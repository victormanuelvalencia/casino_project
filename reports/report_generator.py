from utils.sorting_algorithms import sort_elements_by
from utils.file_administration import read_json
from utils.config import *

def ranking_players_in(criteria):
    # First, sort the player data based on the selected criterion (ascending order)
    sort_elements_by(criteria, PLAYER_FILE)

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
    sort_elements_by(criteria, GAME_FILE)

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

