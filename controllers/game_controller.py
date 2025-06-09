from utils.config import GAME_FILE 
from utils.file_administration import read_json
from utils.sorting_algorithms import sort_elements_by
from models.game import Game

def get_game_fromName(game_name):
    # Sorts the game data stored in the JSON file by the "game_name" field
    sort_elements_by("game_name", GAME_FILE)

    # Reads and loads the content of the games.json file
    games_data = read_json(GAME_FILE)

    # Iterates through each entry in the game data
    for data in games_data:
        # Compares the current game's name with the requested name
        if data["game_name"] == game_name:
            # Converts the matching dictionary into a Game object
            game = Game.from_dict(data)

            # Prints the resulting Game object to the console (for debugging)
            print(game)
            return game

    # If no matching game is found, prints -1 and returns False
    print(-1)
    return False