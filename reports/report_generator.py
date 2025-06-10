from utils.sorting_algorithms import sort_elements_by_bubble, sort_elements_by_merge
from utils.file_administration import read_json
from utils.config import *

def ranking_players_in(criteria):
    """
    Displays the top-ranking players based on a given criterion.
    Sorts player data from a file and prints the top performers in descending order.

    Parameters:
    - criteria: str. The ranking criterion used to sort players.
                Must be one of: "balance", "games_won", or "games_lost".

    Returns:
    - None. Outputs the ranking information directly to the console.
    """

    # First, sort the player data based on the selected criterion (ascending order)
    sort_elements_by_merge(criteria, PLAYER_FILE)

    # Define label variables depending on the selected ranking criterion
    text = ""
    symbol = ""
    stat_type = ""

    if criteria == "balance":
        text = "players with the highest balance"
        symbol = "$"
        stat_type = "Balance"

    if criteria == "games_won":
        text = "top players"
        stat_type = "Games won"

    if criteria == "games_lost":
        text = "players with the most losses"
        stat_type = "Games lost"

    # Read the sorted player data from the file
    players = read_json(PLAYER_FILE)
    n = len(players)

    # Display the top 5 players (from the highest values in the sorted list)
    i = 1
    index = n - 1
    limit = 0
    print(f"\nTop {text}:")

    while index >= 0 and limit < 5:
        player = players[index]
        print(f"{i}. {player['full_name']} (ID: {player['player_id']}) - {stat_type}: {symbol}{player[criteria]:.2f}")
        index -= 1
        i += 1
        limit += 1


def ranking_games_in(criteria):
    sort_elements_by_bubble(criteria, GAME_FILE)

    # Define label variables depending on the selected ranking criterion
    text = ""
    stat_type = ""

    if criteria == "count":
        text = "most played games."
        stat_type = "Times played"

    games = read_json(GAME_FILE)
    n = len(games)
    print(n)
    i = 1
    index = n - 1
    limit = 0
    print(f"\nTop {text}:")

    while index >= 0 and limit < 5:
        game = games[index]
        print(f"{i}. {game['game_name']} - {stat_type}: {game[criteria]:.2f}")
        index -= 1
        i += 1
        limit += 1

