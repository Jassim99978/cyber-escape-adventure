from security.security import get_nonempty_text, get_valid_choice, log_event
from systems.inventory import has_item


def password_challenge(state):
    """Password puzzle challenge. Returns True on success."""
    print("\n=== PASSWORD CHALLENGE ===")
    print("The terminal asks for the server password.")

    if has_item(state, "hidden code"):
        print("Your hidden code gives a hint: cyber123")

    attempts = 0
    while attempts < 3:
        password = get_nonempty_text("Enter server password, or type Q to back out: ", "Terminal password")

        if password.upper() == "Q":
            print("You step away from the terminal.")
            log_event("CHALLENGE_ATTEMPT", f"Puzzle=TerminalLogin; Attempts={attempts}; Player backed out", "FAIL")
            return False

        attempts += 1

        if password == "cyber123":
            print("Access granted.")
            state.flags["password_challenge_complete"] = True
            log_event("CHALLENGE_ATTEMPT", f"Puzzle=TerminalLogin; Attempts={attempts}", "SUCCESS")
            return True

        state.health -= 10
        print(f"Access denied. Security shock activated. Health: {state.health}")
        log_event("CHALLENGE_ATTEMPT", f"Puzzle=TerminalLogin; Attempts={attempts}; Incorrect password", "FAIL")

        if state.health <= 0:
            return False

    print("Too many failed password attempts. The terminal locks for now.")
    return False


def drone_challenge(state):
    """Security drone challenge. Returns True on success."""
    print("\n=== SECURITY DRONE ===")
    print("A security drone scans the area ahead.")
    print("1. Hide")
    print("2. Fight")
    print("3. Run")
    print("4. Flash the drone with the flashlight")

    choice = get_valid_choice("Choose option: ", ["1", "2", "3", "4"], "Security Drone Challenge")

    if choice == "1":
        print("You hide behind a server rack until the drone passes.")
        state.flags["drone_challenge_complete"] = True
        log_event("CHALLENGE_ATTEMPT", "Puzzle=SecurityDrone; Choice=Hide", "SUCCESS")
        return True

    if choice == "2":
        state.health -= 20
        print(f"The drone shocks you before flying away. Health: {state.health}")
        log_event("CHALLENGE_ATTEMPT", "Puzzle=SecurityDrone; Choice=Fight", "FAIL")
        return False

    if choice == "3":
        state.health -= 10
        print(f"You escape, but the drone grazes you. Health: {state.health}")
        state.flags["drone_challenge_complete"] = True
        log_event("CHALLENGE_ATTEMPT", "Puzzle=SecurityDrone; Choice=Run", "SUCCESS")
        return True

    if has_item(state, "flashlight"):
        print("You flash the drone's camera. It loses tracking and powers down.")
        state.flags["drone_challenge_complete"] = True
        log_event("CHALLENGE_ATTEMPT", "Puzzle=SecurityDrone; Choice=Flashlight", "SUCCESS")
        return True

    state.health -= 15
    print(f"You reach for a flashlight, but you do not have one. Health: {state.health}")
    log_event("CHALLENGE_ATTEMPT", "Puzzle=SecurityDrone; Choice=FlashlightMissing", "FAIL")
    return False
