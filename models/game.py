class Game:
    def __init__(self, game_name: str, count: int = 0):
        """
        Initializes a Game instance.

        Parameters:
        - game_name (str): The name of the game.
        - count (int, optional): The number of times the game has been played. Defaults to 0.
        """
        self.game_name = game_name
        self.count = count

    def __str__(self):
        """
        Returns a human-readable string representation of the Game instance,
        indicating the game's name and how many times it has been played.
        """
        return f"Game: {self.game_name} - Times played: {self.count}"

    def to_dict(self):
        """
        Converts the Game instance into a dictionary format,
        suitable for serialization or storage.

        Returns:
        dict: A dictionary containing 'game_name' and 'count' keys.
        """
        return {
            "game_name": self.game_name,
            "count": self.count
        }

    @classmethod
    def from_dict(cls, data):
        """
        Factory method to create a Game instance from a dictionary.

        Parameters:
        - data (dict): A dictionary with keys 'game_name' and optionally 'count'.

        Returns:
        Game: A new instance of the Game class initialized from the dictionary.
        """
        return cls(
            game_name=data["game_name"],
            count=data.get("count", 0)
        )

    def increment_count(self):
        """
        Increments the play count by one,
        tracking how many times the game has been played.
        """
        self.count += 1

    # Getters
    def get_game_name(self):
        """
        Returns the name of the game.
        """
        return self.game_name

    def get_count(self):
        """
        Returns the number of times the game has been played.
        """
        return self.count

    # Setters
    def set_game_name(self, game_name: str):
        """
        Sets or updates the name of the game.

        Parameters:
        - game_name (str): The new name of the game.
        """
        self.game_name = game_name

    def set_count(self, count: int):
        """
        Sets or updates the play count.

        Parameters:
        - count (int): The new count value.
        """
        self.count = count