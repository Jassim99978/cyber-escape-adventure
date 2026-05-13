class GameState:
    """Stores the player's current progress and game status."""

    def __init__(self):
        self.location = "start"
        self.inventory = []
        self.health = 100
        self.flags = {}
        self.game_over = False

    def show_status(self):
        """Print a simple status display for the player."""
        print("\n===== PLAYER STATUS =====")
        print(f"Location: {self.location}")
        print(f"Health: {self.health}")
        print(f"Inventory items: {len(self.inventory)}")
        print("Flags unlocked:", len(self.flags))
        print("=========================")
