# game.py

class Game:
    def __init__(self, game_name: str, count: int = 0):
        self.game_name = game_name
        self.count = count

    def __str__(self):
        return f"Juego: {self.game_name} - Veces jugado: {self.count}"

    def to_dict(self):
        return {
            "game_name": self.game_name,
            "count": self.count
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            game_name=data["game_name"],
            count=data.get("count", 0)
        )

    def increment_count(self):
        self.count += 1

    # Getters
    def get_game_name(self):
        return self.game_name

    def get_count(self):
        return self.count

    # Setters
    def set_game_name(self, game_name: str):
        self.game_name = game_name

    def set_count(self, count: int):
        self.count = count
