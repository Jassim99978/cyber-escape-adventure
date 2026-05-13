from systems.challenges import drone_challenge, password_challenge
from content.npcs import engineer_npc, guard_npc, medic_npc, merchant_npc, scientist_npc
from content.story import story
from engine.state import GameState
from security.save_load import load_game, save_game
from security.security import get_valid_choice, log_event
from systems.inventory import choose_inventory_item, show_inventory, use_item


NPC_EVENTS = {
    "engineer": engineer_npc,
    "scientist": scientist_npc,
    "merchant": merchant_npc,
    "guard": guard_npc,
    "medic": medic_npc,
}


def show_how_to_play():
    """Display basic game instructions."""
    print("\n===== HOW TO PLAY =====")
    print("Choose numbered options to move through the story.")
    print("Use I to view inventory, U to use an item, T to show status, S to save, L to load, and Q to quit.")
    print("Your choices, items, and NPC interactions unlock different paths and endings.")
    print("Security events are written to audit_log.txt.")
    print("=======================")


def give_scene_rewards(state, current_scene):
    """Give scene rewards only once."""
    reward_flag = f"rewarded_{state.location}"

    if "reward" not in current_scene or state.flags.get(reward_flag):
        return

    from systems.inventory import add_item

    for item in current_scene["reward"]:
        add_item(state, item)

    state.flags[reward_flag] = True
    log_event("SCENE_REWARD", f"Scene={state.location}", "SUCCESS")


def run_scene_npc(state, current_scene):
    """Run the NPC interaction attached to a scene.

    NPCs are allowed to repeat. This fixes the problem where a player could visit the
    guard or merchant too early, fail, and then never interact with them again.
    """
    npc_name = current_scene.get("npc")
    if not npc_name:
        return

    npc_function = NPC_EVENTS.get(npc_name)
    if npc_function:
        npc_function(state)


def attempt_security_challenges(state):
    """Run the two required challenges before entering the server room."""
    if not state.flags.get("checkpoint_access"):
        print("\nYou need checkpoint access first. Show the guard a keycard, access chip, or security badge.")
        log_event("SECURITY_ACCESS", "No checkpoint authorization", "FAIL")
        return False

    if state.flags.get("password_challenge_complete") and state.flags.get("drone_challenge_complete"):
        print("\nSecurity challenges are already complete. The server room is open.")
        return True

    if state.flags.get("password_challenge_complete"):
        password_success = True
        print("\nPassword challenge already completed.")
    else:
        password_success = password_challenge(state)
    if state.health <= 0:
        return False

    if state.flags.get("drone_challenge_complete"):
        drone_success = True
        print("\nDrone challenge already completed.")
    else:
        drone_success = drone_challenge(state)
    if state.health <= 0:
        return False

    if password_success and drone_success:
        print("\nBoth security challenges completed. Server room unlocked.")
        state.flags["server_access"] = True
        log_event("SECURITY_ACCESS", "Both challenges completed", "SUCCESS")
        return True

    print("\nSecurity challenge failed. Recover, find hints/items, and try again.")
    log_event("SECURITY_ACCESS", "Challenge failure", "FAIL")
    return False


def can_move_to_scene(state, current_location, next_scene):
    """Check story locks before changing scenes."""
    if current_location == "security_room" and next_scene == "server_room":
        return attempt_security_challenges(state)

    if current_location == "maintenance_tunnel" and next_scene == "ending_scientist":
        if not state.flags.get("helped_scientist"):
            print("\nThe tunnel exit is locked. You need to help the scientist first to get the route code.")
            log_event("PATH_BLOCKED", "Maintenance tunnel escape without scientist", "FAIL")
            return False

        if not state.flags.get("drone_challenge_complete"):
            print("\nA security drone blocks the tunnel exit.")
            if not drone_challenge(state):
                print("\nYou failed to clear the tunnel drone. Try again after recovering.")
                return False

        return True

    return True


def handle_special_action(state, choice):
    """Handle non-number menu actions. Returns True if an action was handled."""
    if choice == "I":
        show_inventory(state)
        log_event("MENU_ACTION", "Viewed inventory", "SUCCESS")
        return True

    if choice == "U":
        item = choose_inventory_item(state)
        if item is not None:
            use_item(state, item)
        return True

    if choice == "T":
        state.show_status()
        log_event("MENU_ACTION", "Viewed status", "SUCCESS")
        return True

    if choice == "S":
        save_game(state)
        return True

    if choice == "L":
        load_game(state)
        return True

    if choice == "Q":
        print("\nThanks for playing.")
        state.game_over = True
        log_event("GAME_END", "Player quit", "SUCCESS")
        return True

    return False


def play_scene(state):
    """Display one scene and process the player's menu choice."""
    if state.location not in story:
        print("\nSave file points to an invalid scene. Returning to start.")
        log_event("LOAD_FIX", f"Invalid scene={state.location}; Reset to start", "FAIL")
        state.location = "start"

    current_scene = story[state.location]

    print("\n" + current_scene["text"])
    print(f"Health: {state.health}")

    give_scene_rewards(state, current_scene)
    run_scene_npc(state, current_scene)

    if state.health <= 0:
        print("\nYour health reached 0. You did not survive.")
        print("\n===== GAME OVER =====")
        state.game_over = True
        log_event("GAME_END", "Player health reached 0", "FAIL")
        return

    if len(current_scene["choices"]) == 0:
        print("\n===== GAME OVER =====")
        state.game_over = True
        log_event("GAME_END", f"Ending={state.location}", "SUCCESS")
        return

    print("\nWhat would you like to do?\n")

    for number, choice in current_scene["choices"].items():
        print(f"{number}. {choice['description']}")

    print("I. View Inventory")
    print("U. Use Item")
    print("T. Show Status")
    print("S. Save Game")
    print("L. Load Game")
    print("Q. Quit")

    valid_choices = list(current_scene["choices"].keys()) + ["I", "U", "T", "S", "L", "Q"]
    player_choice = get_valid_choice("\nEnter choice: ", valid_choices, f"Scene menu: {state.location}")

    if handle_special_action(state, player_choice):
        return

    next_scene = current_scene["choices"][player_choice]["next_scene"]
    old_location = state.location
    if can_move_to_scene(state, old_location, next_scene):
        state.location = next_scene
        log_event("SCENE_CHANGE", f"From={old_location}; To={next_scene}", "SUCCESS")


def start_game(load_existing=False):
    """Start the game loop."""
    state = GameState()

    print("===== CYBER ESCAPE ADVENTURE =====")
    print("Escape the research facility and survive.\n")
    log_event("GAME_START", "Game loop started", "SUCCESS")

    if load_existing:
        loaded = load_game(state)
        if not loaded:
            print("Starting a new game instead.")

    while not state.game_over:
        play_scene(state)
