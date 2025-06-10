import json
from utils.config import *

def read_json(path):
    """
       Reads and returns the contents of a JSON file from the specified path.

       Parameters:
       - path: str. The file system path to the JSON file.

       Returns:
       - The Python object parsed from the JSON file (typically a list or dictionary).
       """

    # Reads and returns the contents of a JSON file from the specified path.
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def write_json(data, path):
    """
    Writes the given data to a JSON file at the specified path.

    Parameters:
    - data: any serializable Python object (typically a list or dictionary).
    - path: str. The file system path where the JSON file will be saved.

    Returns:
    - None. Data is saved directly to the specified file.
    """

    # Writes the given data to a JSON file at the specified path.
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def update_player_in_data(player):
    """
    Updates a player's data in the player JSON file.
    Searches by player ID and replaces the existing record with the latest information.

    Parameters:
    - player: Player object. Must implement get_player_id() and to_dict() methods.

    Returns:
    - None. The updated player data is written to the JSON file.
    """
    players_data = read_json(PLAYER_FILE)

    # Locate the player by their player_id and update their information
    for idx, data in enumerate(players_data):
        if data["player_id"] == player.get_player_id():
            players_data[idx] = player.to_dict()
            break

    # Save the updated data back to the file
    write_json(players_data, PLAYER_FILE)

def update_game_in_data(game):
    """
    Updates a game's data in the game JSON file.
    Searches by game name and replaces the existing record with the latest information.

    Parameters:
    - game: Game object. Must implement get_game_name() and to_dict() methods.

    Returns:
    - None. The updated game data is written to the JSON file.
    """
    games_data = read_json(GAME_FILE)

    # Locate the game by its game_name and update its information
    for idx, data in enumerate(games_data):
        if data["game_name"] == game.get_game_name():
            games_data[idx] = game.to_dict()
            break

    # Save the updated data back to the file
    write_json(games_data, GAME_FILE)

