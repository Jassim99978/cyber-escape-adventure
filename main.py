from engine.game_engine import show_how_to_play, start_game
from security.security import get_valid_choice, log_event


def main_menu():
    """Show the main menu and validate the player's menu input."""
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Start New Game")
        print("2. Load Saved Game")
        print("3. How To Play")
        print("4. Quit")
        print("L. Load Saved Game")
        print("Q. Quit")

        choice = get_valid_choice("Enter choice: ", ["1", "2", "3", "4", "L", "Q", "S"], "Main menu")

        if choice == "1":
            log_event("MAIN_MENU", "Start new game selected", "SUCCESS")
            start_game(load_existing=False)
            break
        if choice in ["2", "L"]:
            log_event("MAIN_MENU", "Load saved game selected", "SUCCESS")
            start_game(load_existing=True)
            break
        if choice == "3":
            log_event("MAIN_MENU", "How to play selected", "SUCCESS")
            show_how_to_play()
        elif choice == "S":
            print("You need to start the game before saving. During gameplay, type S to save.")
            log_event("MAIN_MENU", "Save selected before game start", "FAIL")
        elif choice in ["4", "Q"]:
            print("Goodbye.")
            log_event("MAIN_MENU", "Quit selected", "SUCCESS")
            break


if __name__ == "__main__":
    main_menu()
