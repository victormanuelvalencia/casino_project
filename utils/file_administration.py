import json
from utils.config import *

def read_json(path):
    # Reads and returns the contents of a JSON file from the specified path.
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def write_json(data, path):
    # Writes the given data to a JSON file at the specified path.
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def update_player_in_data(player):
    """
    Searches for a player by ID and updates their data in the JSON file.
    This function can be used across multiple games or modules.
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
    Searches for a game by its name and updates its data in the JSON file.
    This function can be reused in multiple modules that handle games.
    """
    games_data = read_json(GAME_FILE)

    # Locate the game by its game_name and update its information
    for idx, data in enumerate(games_data):
        if data["game_name"] == game.get_game_name():
            games_data[idx] = game.to_dict()
            break

    # Save the updated data back to the file
    write_json(games_data, GAME_FILE)

