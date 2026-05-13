# Flowchart

```text
START
  |
  v
MAIN MENU
  |-- Start New Game --> GAME LOOP
  |-- Load Saved Game --> LOAD SAVE --> GAME LOOP
  |-- How To Play --> MAIN MENU
  |-- Quit --> END

GAME LOOP
  |
  v
CURRENT SCENE
  |-- Show story text
  |-- Give scene rewards once
  |-- Run scene NPC interaction when present
  |-- Validate menu input
  |-- Save / Load / Inventory / Use Item / Status / Quit

STORY PATHS
  |
  |-- Path 1: Find the Keycard
  |     start -> storage_room -> hallway -> security_room -> guard approval
  |     -> password_challenge -> drone_challenge -> server_room
  |
  |-- Path 2: Hack the Terminal
  |     hallway -> engineer_room or scientist_room for hints/items
  |     -> security_room -> server_room -> ending_hacker
  |
  |-- Path 3: Help the Scientist
        start/hallway -> scientist_room -> maintenance_tunnel
        -> drone_challenge if needed -> ending_scientist

SERVER ROOM ENDINGS
  |-- Hack terminal -> ending_hacker
  |-- Destroy servers -> ending_destroy
```
