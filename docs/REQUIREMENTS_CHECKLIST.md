# Requirements Checklist

| PDF Requirement | Project Match |
|---|---|
| At least 3 story paths | Storage/keycard path, terminal/security path, scientist/tunnel path |
| At least 3 different endings | `ending_hacker`, `ending_destroy`, `ending_scientist` in `content/story.py` |
| Clear beginning, middle, and end | Start scene, hallway/security/tunnel middle paths, final ending scenes |
| At least 5 locations or major events | start, storage_room, hallway, engineer_room, merchant_room, scientist_room, maintenance_tunnel, security_room, server_room |
| At least 5 NPCs | engineer, scientist, merchant, guard, medic in `content/npcs.py` |
| NPCs have meaningful interactions | clue, items, trade, access unlock, healing, route unlocking |
| Inventory system | `systems/inventory.py` has add, remove, view, use, item choice menu, and item checks |
| Minimum 5 items | medkit, keycard, battery, energy drink, flashlight, access chip, hidden code, security badge |
| Items have purposes | healing, checkpoint access, trading, password hint, drone help, route/story support |
| At least 2 challenges | password challenge and security drone challenge in `challenges/challenges.py` |
| Clear instructions | Main menu and `How To Play` screen |
| Safe invalid input handling | `get_valid_choice()` re-prompts invalid input in menus/NPCs/challenges |
| try/except where needed | input helpers and save/load file handling use exception handling |
| Audit log file named `audit_log.txt` | `security/security.py` writes timestamped logs inside the project folder |
| Log game start/end | `engine/game_engine.py` logs game start and game end |
| Log save/load attempts | `security/save_load.py` logs success/failure/tamper results |
| Log challenge attempts | `challenges/challenges.py` logs success/failure results |
| Save/load support | `security/save_load.py` saves/loads JSON game state |
| Tamper detection | Save file stores SHA-256 hash and rejects mismatch |
| Modular role-based files | main.py, engine/, content/, systems/, challenges/, security/ |
| README checklist | `README.md` includes features, paths, endings, locations, NPCs, items, challenges, Cyber Pack |
| Flowchart in docs | `docs/flowchart.png` and `docs/FLOWCHART.md` |
| Individual survey | `docs/INDIVIDUAL_SURVEY_TEMPLATE.md` |

## Cannot Be Faked Inside a Zip

The PDF also requires GitHub collaboration evidence: PRs, commits, reviews, issues, and a tagged release. Those must be done in GitHub itself. This folder includes a `docs/GITHUB_COLLABORATION_CHECKLIST.md` file so the team can track it honestly.
