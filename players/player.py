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

    """
    Método que convierte cada uno atributos del objeto a una clave de diccionario, retornando
    el objeto completo como un diccionario, el cual es mucho mas fácil para manipular y almacenar
    """
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

    """
    Método utilizado para convertir un diccionario almacenado en el players.json en un 
    objeto de la clase Player, lo usamos para reconstruirlo y poder manipular los jugadores
    como objeto, para facilitar el uso de métodos como update_player
    """
    @classmethod
    def from_dict(cls, data): # Aquí cls se refiere a la propia clase Player y data es el diccionario
        player = cls( # Se crea una nueva instancia de la clase Player.
            # Asignamos los valores de las claves del diccionario a los
            # atributos del objeto
            full_name=data["full_name"],
            player_id=data["player_id"],
            balance=data["balance"]
        )
        # Aquí asignamos los valores de las claves del diccionario sí existen, sino les asigna 0
        player.history = Stack(data.get("history", [])) # Aquí lo convertimos en una pila, y sino
                                                        # lo mandamos como una pila vacia

        player.games_won = data.get("games_won", 0)
        player.games_lost = data.get("games_lost", 0)
        player.total_bet = data.get("total_bet", 0)
        return player
    """
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
    """
    # Getters
    def get_full_name(self):
        return self.full_name

    def get_player_id(self):
        return self.player_id

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history

    def get_games_won(self):
        return self.games_won

    def get_games_lost(self):
        return self.games_lost

    def get_total_bet(self):
        return self.total_bet

    # Setters
    def set_full_name(self, full_name: str):
        self.full_name = full_name

    def set_player_id(self, player_id: str):
        self.player_id = player_id

    def set_balance(self, balance: float):
        self.balance = balance

    def set_history(self, history_stack: Stack):
        self.history = history_stack

    def set_games_won(self, games_won: int):
        self.games_won = games_won

    def set_games_lost(self, games_lost: int):
        self.games_lost = games_lost

    def set_total_bet(self, total_bet: float):
        self.total_bet = total_bet
