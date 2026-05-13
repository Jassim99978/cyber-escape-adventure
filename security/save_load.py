import hashlib
import json
import os
from security.security import log_event

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAVE_FILE = os.path.join(BASE_DIR, "savegame.json")


def create_hash(data):
    """Create a SHA-256 hash for the saved game data."""
    json_data = json.dumps(data, sort_keys=True)
    return hashlib.sha256(json_data.encode("utf-8")).hexdigest()


def save_game(state):
    """Save the current game state with a tamper-detection hash."""
    data = {
        "location": state.location,
        "inventory": state.inventory,
        "health": state.health,
        "flags": state.flags,
        "game_over": state.game_over,
    }

    save_data = {
        "game": data,
        "hash": create_hash(data),
    }

    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(save_data, file, indent=4)

        log_event("SAVE_ATTEMPT", f"File={SAVE_FILE}", "SUCCESS")
        print("Game saved.")
        return True
    except PermissionError:
        print("Save failed because this folder is protected. Move the project to Downloads/Desktop and run it again.")
        log_event("SAVE_ATTEMPT", "Permission denied", "FAIL")
        return False


def load_game(state):
    """Load a saved game only if the save file has not been changed."""
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            save_data = json.load(file)

        data = save_data["game"]
        saved_hash = save_data["hash"]
        new_hash = create_hash(data)

        if saved_hash != new_hash:
            print("Tampered save detected. Load blocked.")
            log_event("LOAD_ATTEMPT", "Reason=SAVE_TAMPERED", "FAIL")
            return False

        location = data.get("location", "start")
        inventory = data.get("inventory", [])
        health = data.get("health", 100)
        flags = data.get("flags", {})

        if not isinstance(inventory, list) or not isinstance(flags, dict):
            raise ValueError("Invalid save data types")

        state.location = location
        state.inventory = inventory
        state.health = int(health)
        state.flags = flags
        state.game_over = bool(data.get("game_over", False))

        log_event("LOAD_ATTEMPT", f"Loaded location={state.location}", "SUCCESS")
        print("Game loaded.")
        return True

    except FileNotFoundError:
        print("No save file found. Save the game first by typing S during gameplay.")
        log_event("LOAD_ATTEMPT", "Reason=NO_SAVE_FILE", "FAIL")
        return False
    except (KeyError, json.JSONDecodeError, ValueError, TypeError):
        print("Save file is damaged or invalid.")
        log_event("LOAD_ATTEMPT", "Reason=INVALID_SAVE_FILE", "FAIL")
        return False
