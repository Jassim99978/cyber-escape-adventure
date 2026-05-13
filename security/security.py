import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIT_FILE = os.path.join(BASE_DIR, "audit_log.txt")


def log_event(event_type, detail="", result=""):
    """Write one timestamped security/game event to audit_log.txt."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts = [timestamp, event_type]

    if result:
        parts.append(result)
    if detail:
        parts.append(detail)

    try:
        with open(AUDIT_FILE, "a", encoding="utf-8") as file:
            file.write(" - ".join(parts) + "\n")
    except PermissionError:
        print("Warning: Could not write to audit_log.txt because of folder permissions.")


def get_valid_choice(prompt, valid_choices, context="menu"):
    """Keep asking until the player enters one of the allowed choices."""
    normalized_choices = [str(choice).upper() for choice in valid_choices]

    while True:
        try:
            user_input = input(prompt).strip()
            normalized_input = user_input.upper()

            if normalized_input in normalized_choices:
                return normalized_input

            allowed = ", ".join(str(choice) for choice in valid_choices)
            print(f"Invalid choice. Please enter one of these options: {allowed}.")
            log_event("INPUT_INVALID", f'Context={context}; Input="{user_input}"', "FAIL")

        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled. Returning safely.")
            log_event("INPUT_ERROR", f"Context={context}; Input interrupted", "FAIL")
            return str(valid_choices[-1]).upper()


def get_nonempty_text(prompt, context="text input"):
    """Ask for text and reject blank input."""
    while True:
        try:
            value = input(prompt).strip()
            if value:
                return value
            print("Invalid input. Please type something.")
            log_event("INPUT_INVALID", f"Context={context}; Blank input", "FAIL")
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled.")
            log_event("INPUT_ERROR", f"Context={context}; Input interrupted", "FAIL")
            return "Q"
