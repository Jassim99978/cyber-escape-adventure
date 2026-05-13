story = {
    "start": {
        "text": "You wake up inside a locked research facility. Emergency lights flash across the walls.",
        "choices": {
            "1": {"description": "Search the storage room", "next_scene": "storage_room"},
            "2": {"description": "Go to the main hallway", "next_scene": "hallway"},
            "3": {"description": "Follow a voice calling for help", "next_scene": "scientist_room"},
        },
    },
    "storage_room": {
        "text": "You search dusty storage crates and find useful supplies.",
        "reward": ["medkit", "keycard", "battery", "energy drink", "flashlight"],
        "choices": {
            "1": {"description": "Return to the hallway", "next_scene": "hallway"},
        },
    },
    "hallway": {
        "text": "A dark hallway connects the major areas of the facility.",
        "choices": {
            "1": {"description": "Visit the engineer", "next_scene": "engineer_room"},
            "2": {"description": "Visit the merchant", "next_scene": "merchant_room"},
            "3": {"description": "Enter the security checkpoint", "next_scene": "security_room"},
            "4": {"description": "Follow the voice to the scientist", "next_scene": "scientist_room"},
            "5": {"description": "Search the maintenance tunnel", "next_scene": "maintenance_tunnel"},
        },
    },
    "engineer_room": {
        "text": "An engineer studies broken security panels and damaged wires.",
        "npc": "engineer",
        "choices": {
            "1": {"description": "Return to the hallway", "next_scene": "hallway"},
        },
    },
    "merchant_room": {
        "text": "A nervous merchant hides behind supply crates.",
        "npc": "merchant",
        "choices": {
            "1": {"description": "Return to the hallway", "next_scene": "hallway"},
        },
    },
    "scientist_room": {
        "text": "A trapped scientist calls for help behind a collapsed lab doorway.",
        "npc": "scientist",
        "choices": {
            "1": {"description": "Go to the maintenance tunnel", "next_scene": "maintenance_tunnel"},
            "2": {"description": "Return to the hallway", "next_scene": "hallway"},
        },
    },
    "maintenance_tunnel": {
        "text": "The maintenance tunnel is dark, narrow, and separated from the main security system.",
        "npc": "medic",
        "choices": {
            "1": {"description": "Attempt the tunnel escape", "next_scene": "ending_scientist"},
            "2": {"description": "Return to the hallway", "next_scene": "hallway"},
        },
    },
    "security_room": {
        "text": "A guarded security checkpoint blocks the server wing.",
        "npc": "guard",
        "choices": {
            "1": {"description": "Attempt the server-room security challenges", "next_scene": "server_room"},
            "2": {"description": "Return to the hallway", "next_scene": "hallway"},
        },
    },
    "server_room": {
        "text": "Rows of servers control the alarms, doors, and security drones.",
        "choices": {
            "1": {"description": "Hack the terminal and escape quietly", "next_scene": "ending_hacker"},
            "2": {"description": "Destroy the servers and force an escape", "next_scene": "ending_destroy"},
        },
    },
    "ending_hacker": {
        "text": "Ending 1: You disable the alarms, unlock the security gate, and escape quietly.",
        "choices": {},
    },
    "ending_destroy": {
        "text": "Ending 2: You destroy the servers. The facility collapses behind you as you escape.",
        "choices": {},
    },
    "ending_scientist": {
        "text": "Ending 3: You and the scientist escape safely through the maintenance tunnel.",
        "choices": {},
    },
}
