# Cyber Escape Adventure

## Team Members
- Eisa Syed
- Jasmin Mclaren
- Braden Fleckenstien
- Jassem Hussain

---

## How to Run the Game

Make sure Python 3 is installed.

Open the project folder in a terminal, then run:

```bash
python main.py
```

Do not run the game from inside a protected folder like `C:\Program Files`. Put the project in Downloads, Desktop, or another normal user folder.

---

## Project Description

Cyber Escape Adventure is a text-based adventure game where the player wakes up inside a locked research facility. The player must explore different areas, interact with NPCs, collect items, complete challenges, and make choices that lead to different endings.

The game includes the required Cyber Pack features: safe input validation, audit logging, and save/load with tamper detection.

---

## Core Game Features Included

- At least 3 different story paths
- At least 3 different endings
- Clear beginning, middle, and end
- 5+ locations or major events
- 5 NPC interactions
- Inventory system with 5+ usable items
- 2 challenges with success/failure outcomes
- Safe input handling
- Audit logging to `audit_log.txt`
- Save/load system with tamper detection

---

## Story Paths and Endings

### Story Path 1: Find the Keycard
The player searches the storage room, collects a keycard, and uses it to pass the security checkpoint.

### Story Path 2: Hack the Terminal
The player reaches the server room, completes the password and drone challenges, hacks the facility terminal, and escapes through the security gate.

### Story Path 3: Help the Scientist
The player helps the trapped scientist, receives the hidden code and security badge, then escapes through the maintenance tunnel.

---

## Endings

### Hacker Ending
The player successfully hacks the facility systems, disables the alarms, and escapes quietly through the security gate.

### Destroy Ending
The player destroys the server systems. The facility begins collapsing, but the player escapes after forcing the doors open.

### Scientist Escape Ending
The player helps the scientist and escapes safely through the maintenance tunnel.

---

## Locations / Major Events

1. **Start Room**  
   The player wakes up inside the locked research facility and chooses where to go first.

2. **Storage Room**  
   The player collects useful inventory items such as a keycard, medkit, battery, energy drink, and flashlight.

3. **Hallway**  
   The central area that connects the player to the major story paths.

4. **Engineer Room**  
   The player meets the engineer, who explains the rogue AI and can give an access chip.

5. **Merchant Room**  
   The player can trade a battery for a medkit and receive advice about drones.

6. **Scientist Room**  
   The player can help the trapped scientist and unlock the hidden tunnel path.

7. **Maintenance Tunnel**  
   The player can receive medical help and escape through the scientist route if the scientist was helped.

8. **Security Room**  
   The player meets the security guard and must show authorization before trying to enter the server wing.

9. **Server Room**  
   The player completes the required challenges and chooses either the hacker ending or destroy ending.

---

## NPCs

### Engineer
- **Location:** Engineer Room  
- **Purpose:** Gives information about the rogue facility AI and can give the player an access chip.

### Scientist
- **Location:** Scientist Room  
- **Purpose:** Unlocks the scientist story path, gives the hidden code, and gives the security badge if helped.

### Merchant
- **Location:** Merchant Room  
- **Purpose:** Trades a battery for a medkit and gives advice about the drone challenge.

### Security Guard
- **Location:** Security Room  
- **Purpose:** Checks the keycard, access chip, or security badge before allowing server-room challenge access.

### Medic
- **Location:** Maintenance Tunnel  
- **Purpose:** Restores health once and gives advice about the tunnel escape route.

---

## Inventory Items

### Keycard
Used to pass the security checkpoint.

### Access Chip
Given by the engineer and used as another way to pass the security checkpoint.

### Security Badge
Given by the scientist and used as another way to pass the security checkpoint.

### Hidden Code
Gives the player a hint for the server password challenge.

### Battery
Can be traded with the merchant for a medkit.

### Medkit
Restores 25 health when used.

### Energy Drink
Restores 10 health when used.

### Flashlight
Helps the player in the maintenance tunnel and can be used to beat the drone challenge.

---

## Challenges

### Password Challenge
- **Location:** Server-room access event  
- **Goal:** Enter the correct server password.  
- **Success:** The player passes the terminal login challenge.  
- **Failure:** The player loses health. After too many failed attempts, the terminal locks for that attempt.

### Drone Challenge
- **Location:** Server-room access event and tunnel escape route  
- **Goal:** Choose how to survive a security drone encounter.  
- **Success:** The player avoids or disables the drone.  
- **Failure:** The player loses health and may need to try again.

---

## Cyber Pack Features

### 1. Input Validation and Safe Error Handling
The game uses validated menus and does not crash when the player types invalid input. The player is re-prompted until a valid option is entered.

### 2. Audit Logging
The game writes important security-related events to:

```text
audit_log.txt
```

Logged events include game start, game end, invalid input, challenge attempts, save attempts, load attempts, tamper detection, item usage, NPC interactions, and scene changes.

### 3. Save / Load With Tamper Check
The game saves progress to:

```text
savegame.json
```

The save file includes a SHA-256 hash. When loading, the game recalculates the hash. If the save file was edited, the hash will not match and the game blocks the load.

---

## Flowchart

The project includes a flowchart showing story branches and endings:

```text
docs/flowchart.png
```

---

## GitHub Collaboration Requirements

The GitHub repository should show:

- No direct pushes to the main branch
- Pull requests for code changes
- At least 2 pull requests per student
- At least 6 commits per student
- At least 2 PR reviews per student
- At least 8 GitHub issues for the team
- A tagged release named `v1.0` or a clearly labeled final commit

---

## Individual Submission Reminder

Each student should also submit a short individual paragraph answering:

1. What did you personally code?
2. What files/modules did you work on?
3. What functions or features did you add?
4. What teamwork challenge did your group face, and how did you solve it?
5. Teammate contribution scores from 1-5 with short reasons.
