# Clase Jugador con historial (pila) y datos personales

from utils.stack import Stack
import datetime

class Player:
    def __init__(self, full_name: str, player_id: str, balance: float):
        self.full_name = full_name
        self.player_id = player_id
        self.balance = balance
        self.history = Stack()
        self.games_won = 0
        self.games_lost = 0
        self.total_bet = 0

    def __str__(self):
        return f"{self.full_name} (ID: {self.player_id}) - Balance: ${self.balance:.2f}"

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "player_id": self.player_id,
            "balance": self.balance,
            "history": self.history.to_list(),
            "games_won": self.games_won,
            "games_lost": self.games_lost,
            "total_bet": self.total_bet
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(
            full_name=data["full_name"],
            player_id=data["player_id"],
            balance=data["balance"]
        )
        player.history = Stack(data.get("history", []))
        player.games_won = data.get("games_won", 0)
        player.games_lost = data.get("games_lost", 0)
        player.total_bet = data.get("total_bet", 0)
        return player

    def add_history(self, action: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.push(f"[{timestamp}] {action}")

    def update_balance(self, amount: float):
        self.balance += amount
        self.add_history(f"Balance updated by ${amount:.2f}. New balance: ${self.balance:.2f}")

    def bet(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient balance to place bet.")
        self.balance -= amount
        self.total_bet += amount
        self.add_history(f"Bet of ${amount:.2f} placed. Remaining balance: ${self.balance:.2f}")