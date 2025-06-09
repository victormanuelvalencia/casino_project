from utils.stack import Stack
import datetime

class Player:
    def __init__(self, full_name: str, player_id: str, balance: float):
        """
        Initializes a new Player instance.

        Parameters:
        - full_name (str): The full name of the player.
        - player_id (str): Unique identifier for the player.
        - balance (float): The player's current balance.
        """
        self.full_name = full_name
        self.player_id = player_id
        self.balance = balance
        self.history = Stack()          # Stack to maintain player's action history
        self.games_won = 0              # Counter for games won
        self.games_lost = 0             # Counter for games lost
        self.total_bet = 0              # Total amount bet by the player

    def __str__(self):
        """
        Returns a human-readable string representation of the player,
        including name, ID, and balance formatted to 2 decimals.
        """
        return f"{self.full_name} (ID: {self.player_id}) - Balance: ${self.balance:.2f}"

    def to_dict(self):
        """
        Converts the Player instance into a dictionary.

        This facilitates easy serialization and storage, by
        representing all attributes, including the history converted to a list.

        Returns:
        dict: Dictionary containing all player attributes.
        """
        return {
            "full_name": self.full_name,
            "player_id": self.player_id,
            "balance": self.balance,
            "history": self.history.to_list(),  # Convert stack to list for serialization
            "games_won": self.games_won,
            "games_lost": self.games_lost,
            "total_bet": self.total_bet
        }

    @classmethod
    def from_dict(cls, data):
        """
        Class method to reconstruct a Player instance from a dictionary.

        Used primarily when loading player data from storage (e.g., JSON files).
        Ensures the player object can be manipulated using class methods.

        Parameters:
        - data (dict): Dictionary with player data.

        Returns:
        Player: A new Player instance initialized with provided data.
        """
        player = cls(
            full_name=data["full_name"],
            player_id=data["player_id"],
            balance=data["balance"]
        )
        # Restore history stack, or initialize empty if missing
        player.history = Stack(data.get("history", []))

        # Restore additional attributes or default to zero if not present
        player.games_won = data.get("games_won", 0)
        player.games_lost = data.get("games_lost", 0)
        player.total_bet = data.get("total_bet", 0)
        return player

    # The following commented methods are examples for balance updates and bets,
    # demonstrating encapsulation and history logging for transactions.

    """
    def update_balance(self, amount: float):
        self.balance += amount
        self.add_history(f"Balance updated by ${amount:.2f}. New balance: ${self.balance:.2f}")

    def bet(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient balance to place bet.")
        self.balance -= amount
        self.total_bet += amount
        self.add_history(f"Bet of ${amount:.2f} placed. Remaining balance: ${self.balance:.2f}")
    """

    # Getters
    def get_full_name(self):
        # Returns the player's full name.
        return self.full_name

    def get_player_id(self):
        # Returns the player's unique ID.
        return self.player_id

    def get_balance(self):
        # Returns the player's current balance.
        return self.balance

    def get_history(self):
        """
        Prints the action history of the player.

        Uses the stack's show method to display the stored actions.
        """
        print(f"\nHistory of player {self.full_name} (ID: {self.player_id}):")
        self.history.show()

    def get_games_won(self):
        # Returns the total games won by the player.
        return self.games_won

    def get_games_lost(self):
        # Returns the total games lost by the player.
        return self.games_lost

    def get_total_bet(self):
        # Returns the total amount bet by the player.
        return self.total_bet

    # Setters
    def set_full_name(self, full_name: str):
        # Sets or updates the player's full name.
        self.full_name = full_name

    def set_player_id(self, player_id: str):
        # Sets or updates the player's unique ID.
        self.player_id = player_id

    def set_balance(self, balance: float):
        # Sets or updates the player's balance.
        self.balance = balance

    def set_history(self, action: str):
        """
        Adds a new action to the player's history stack.

        Parameters:
        - action (str): A string describing the action to log.
        """
        self.history.push(f"{action}")

    def set_games_won(self, games_won: int):
        # Sets or updates the total number of games won.
        self.games_won = games_won

    def set_games_lost(self, games_lost: int):
        # Sets or updates the total number of games lost.
        self.games_lost = games_lost

    def set_total_bet(self, total_bet: float):
        # Sets or updates the total amount bet.
        self.total_bet = total_bet
