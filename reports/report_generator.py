# reportes/reportes.py (por ejemplo)

from utils.sorting_algorithms import sort_elements_by
from utils.file_administration import read_json
from utils.config import *

def ranking_players_in(criteria):
    # Primero ordenamos por saldo (menor a mayor)
    sort_elements_by(criteria, PLAYER_FILE)

    text = ""
    sing = ""
    type = ""

    if criteria == "balance":
        text = "players with more balance"
        sing = "$"
        type = "Balance"

    if criteria == "games_won":
        text = "best players"
        type = "Games won"

    if criteria == "games_lost":
        text = "players with more loses"
        type = "Games lost"

    # Luego leemos los datos ya ordenados
    players = read_json(PLAYER_FILE)
    n = len(players)
    # Mostramos los últimos 5 jugadores (los de mayor saldo)
    i = 1
    index = n - 1

    print(f"\nTop {text}:")

    while index != 0:
        player = players[index]
        print(f"{i}. {player['full_name']} (ID: {player['player_id']}) - {type}: {sing}{player[criteria]:.2f}")

        index -= 1
        i += 1



