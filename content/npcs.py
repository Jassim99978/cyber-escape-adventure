from security.security import get_valid_choice, log_event
from systems.inventory import add_item, has_item, remove_item


def engineer_npc(state):
    """Engineer NPC gives story information and an access chip."""
    print("\nEngineer: You're alive? The facility AI locked everyone inside after the power surge.")
    print("1. Ask what happened")
    print("2. Ask for supplies")
    print("3. Leave")

    choice = get_valid_choice("> ", ["1", "2", "3"], "Engineer NPC")

    if choice == "1":
        print("\nEngineer: The AI controls the doors from the server room. You need authorization first.")
        state.flags["learned_truth"] = True
        log_event("NPC_INTERACTION", "NPC=Engineer; Learned truth", "SUCCESS")
    elif choice == "2":
        if not state.flags.get("engineer_gave_chip"):
            print("\nEngineer: Take this access chip. It should help at the checkpoint.")
            add_item(state, "access chip")
            state.flags["engineer_gave_chip"] = True
            state.flags["helped_engineer"] = True
            log_event("NPC_INTERACTION", "NPC=Engineer; Gave access chip", "SUCCESS")
        else:
            print("\nEngineer: I already gave you my only access chip.")
            log_event("NPC_INTERACTION", "NPC=Engineer; Already gave chip", "FAIL")
    else:
        print("\nYou leave the engineer behind.")
        log_event("NPC_INTERACTION", "NPC=Engineer; Player left", "SUCCESS")


def scientist_npc(state):
    """Scientist NPC unlocks the hidden code and scientist path."""
    print("\nScientist: Please help me. I know a hidden tunnel out of here.")
    print("1. Help scientist")
    print("2. Ask for information")
    print("3. Ignore scientist")

    choice = get_valid_choice("> ", ["1", "2", "3"], "Scientist NPC")

    if choice == "1":
        if not state.flags.get("helped_scientist"):
            print("\nYou move debris away from the door and help the scientist escape.")
            print("Scientist: Thank you. Take this hidden code and security badge.")
            add_item(state, "hidden code")
            add_item(state, "security badge")
            state.flags["helped_scientist"] = True
            log_event("NPC_INTERACTION", "NPC=Scientist; Scientist helped", "SUCCESS")
        else:
            print("\nScientist: You already helped me. The tunnel is still available.")
            log_event("NPC_INTERACTION", "NPC=Scientist; Already helped", "SUCCESS")
    elif choice == "2":
        print("\nScientist: The terminal password is hidden in the code I can give you if you help me.")
        state.flags["scientist_hint"] = True
        log_event("NPC_INTERACTION", "NPC=Scientist; Gave hint", "SUCCESS")
    else:
        print("\nYou walk away from the scientist.")
        log_event("NPC_INTERACTION", "NPC=Scientist; Ignored", "SUCCESS")


def merchant_npc(state):
    """Merchant NPC trades battery for a medkit."""
    print("\nMerchant: I trade supplies. A battery is worth one medkit.")
    print("1. Trade battery for medkit")
    print("2. Ask for advice")
    print("3. Leave")

    choice = get_valid_choice("> ", ["1", "2", "3"], "Merchant NPC")

    if choice == "1":
        if has_item(state, "battery"):
            remove_item(state, "battery")
            add_item(state, "medkit")
            print("\nTrade completed.")
            log_event("NPC_INTERACTION", "NPC=Merchant; Trade completed", "SUCCESS")
        else:
            print("\nYou do not have a battery yet.")
            log_event("NPC_INTERACTION", "NPC=Merchant; Missing battery", "FAIL")
    elif choice == "2":
        print("\nMerchant: Use a flashlight in the tunnel. Drones hate sudden light.")
        state.flags["merchant_hint"] = True
        log_event("NPC_INTERACTION", "NPC=Merchant; Gave drone hint", "SUCCESS")
    else:
        print("\nYou leave the merchant.")
        log_event("NPC_INTERACTION", "NPC=Merchant; Player left", "SUCCESS")


def guard_npc(state):
    """Guard NPC checks authorization before server access."""
    print("\nGuard: Access to the server wing is restricted.")
    print("1. Show keycard")
    print("2. Show access chip")
    print("3. Show security badge")
    print("4. Leave")

    choice = get_valid_choice("> ", ["1", "2", "3", "4"], "Guard NPC")

    if choice == "1":
        if has_item(state, "keycard"):
            print("\nGuard: Keycard accepted. You may attempt the security challenges.")
            state.flags["checkpoint_access"] = True
            log_event("NPC_INTERACTION", "NPC=Guard; Accepted keycard", "SUCCESS")
        else:
            print("\nGuard: You do not have a keycard.")
            log_event("NPC_INTERACTION", "NPC=Guard; Missing keycard", "FAIL")
    elif choice == "2":
        if has_item(state, "access chip"):
            print("\nGuard: Access chip accepted. You may attempt the security challenges.")
            state.flags["checkpoint_access"] = True
            log_event("NPC_INTERACTION", "NPC=Guard; Accepted access chip", "SUCCESS")
        else:
            print("\nGuard: You do not have an access chip.")
            log_event("NPC_INTERACTION", "NPC=Guard; Missing access chip", "FAIL")
    elif choice == "3":
        if has_item(state, "security badge"):
            print("\nGuard: Security badge accepted. You may attempt the security challenges.")
            state.flags["checkpoint_access"] = True
            log_event("NPC_INTERACTION", "NPC=Guard; Accepted security badge", "SUCCESS")
        else:
            print("\nGuard: You do not have a security badge.")
            log_event("NPC_INTERACTION", "NPC=Guard; Missing security badge", "FAIL")
    else:
        print("\nYou leave the checkpoint.")
        log_event("NPC_INTERACTION", "NPC=Guard; Player left", "SUCCESS")


def medic_npc(state):
    """Medic NPC restores health once, then gives advice afterward."""
    print("\nMedic: You look injured. I can patch you up once.")
    print("1. Receive treatment")
    print("2. Ask about the tunnel")
    print("3. Leave")

    choice = get_valid_choice("> ", ["1", "2", "3"], "Medic NPC")

    if choice == "1":
        if not state.flags.get("medic_used"):
            old_health = state.health
            state.health = min(100, state.health + 20)
            state.flags["medic_used"] = True
            print(f"\nHealth restored: {old_health} -> {state.health}.")
            log_event("NPC_INTERACTION", "NPC=Medic; Healed player", "SUCCESS")
        else:
            print("\nMedic: I already used my supplies on you.")
            log_event("NPC_INTERACTION", "NPC=Medic; Supplies already used", "FAIL")
    elif choice == "2":
        print("\nMedic: The safe tunnel exit only opens after the scientist gives you the route code.")
        state.flags["medic_hint"] = True
        log_event("NPC_INTERACTION", "NPC=Medic; Gave tunnel hint", "SUCCESS")
    else:
        print("\nYou leave the medic.")
        log_event("NPC_INTERACTION", "NPC=Medic; Player left", "SUCCESS")
