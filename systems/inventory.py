from security.security import get_valid_choice, log_event


def normalize_item(item):
    """Use one consistent item format."""
    return item.lower().strip()


def add_item(state, item):
    """Add an item to the player's inventory if it is not already there."""
    item = normalize_item(item)
    if item not in state.inventory:
        state.inventory.append(item)
        print(f"\nYou collected: {item}")
        log_event("ITEM_COLLECTED", f"Item={item}", "SUCCESS")
    else:
        print(f"\n{item} is already in your inventory.")


def remove_item(state, item):
    """Remove an item from the inventory."""
    item = normalize_item(item)
    if item in state.inventory:
        state.inventory.remove(item)
        print(f"\n{item} removed from inventory.")
        log_event("ITEM_REMOVED", f"Item={item}", "SUCCESS")
        return True

    print("\nItem not found.")
    return False


def has_item(state, item):
    """Return True if the player has the selected item."""
    return normalize_item(item) in state.inventory


def show_inventory(state):
    """Display the player's inventory."""
    print("\n===== INVENTORY =====")

    if len(state.inventory) == 0:
        print("Inventory empty.")
    else:
        for item in state.inventory:
            print("-", item)

    print("=====================")


def choose_inventory_item(state):
    """Let the player choose an item by number."""
    if not state.inventory:
        print("\nInventory empty.")
        return None

    print("\nChoose an item to use:")
    for index, item in enumerate(state.inventory, start=1):
        print(f"{index}. {item}")
    print("B. Back")

    valid_choices = [str(i) for i in range(1, len(state.inventory) + 1)] + ["B"]
    choice = get_valid_choice("Enter choice: ", valid_choices, "Use inventory item")

    if choice == "B":
        return None

    return state.inventory[int(choice) - 1]


def use_item(state, item):
    """Use an inventory item if it has an effect."""
    item = normalize_item(item)

    if item not in state.inventory:
        print("\nItem not found.")
        log_event("ITEM_USED", f"Item={item}; Item missing", "FAIL")
        return False

    if item == "medkit":
        old_health = state.health
        state.health = min(100, state.health + 25)
        print("\nYou used a medkit.")
        print(f"Health: {old_health} -> {state.health}")
        remove_item(state, item)
        log_event("ITEM_USED", "Item=medkit; Health restored", "SUCCESS")
        return True

    if item == "energy drink":
        old_health = state.health
        state.health = min(100, state.health + 10)
        print("\nYou used an energy drink.")
        print(f"Health: {old_health} -> {state.health}")
        remove_item(state, item)
        log_event("ITEM_USED", "Item=energy drink; Health restored", "SUCCESS")
        return True

    if item == "keycard":
        print("\nThe keycard proves you can enter the security checkpoint.")
        log_event("ITEM_USED", "Item=keycard; Access clue shown", "SUCCESS")
        return True

    if item == "access chip":
        print("\nThe access chip can also prove authorization at the checkpoint.")
        log_event("ITEM_USED", "Item=access chip; Access clue shown", "SUCCESS")
        return True

    if item == "security badge":
        print("\nThe security badge can help convince the guard to let you pass.")
        log_event("ITEM_USED", "Item=security badge; Access clue shown", "SUCCESS")
        return True

    if item == "hidden code":
        print("\nThe hidden code says: Server password = cyber123.")
        log_event("ITEM_USED", "Item=hidden code; Password hint shown", "SUCCESS")
        return True

    if item == "battery":
        print("\nThe battery can be traded with the merchant for a medkit.")
        log_event("ITEM_USED", "Item=battery; Trade clue shown", "SUCCESS")
        return True

    if item == "flashlight":
        print("\nThe flashlight helps you see in the maintenance tunnel and hide from drones.")
        state.flags["flashlight_ready"] = True
        log_event("ITEM_USED", "Item=flashlight; Flag=flashlight_ready", "SUCCESS")
        return True

    print("\nNothing happens.")
    log_event("ITEM_USED", f"Item={item}; No effect", "FAIL")
    return False
