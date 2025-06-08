# Burbuja, selección, inserción, mezcla
# utils/data_management.py
import json
from utils.file_administration import read_json, write_json


# Algoritmo de ordenamiento burbuja, pero con los nombres
# Funciona por medio de codigo ASCII
def sort_ids_alphabetically():
    players = read_json()
    n = len(players)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Los hacemos minuscla para que no se confunda el codigo entre mayusculas
            # y minusculas
            nombre_actual = players[j].get("player_id", None).lower()
            nombre_siguiente = players[j + 1].get("player_id", None).lower()
            if nombre_actual > nombre_siguiente:
                # Intercambiar posiciones
                players[j], players[j + 1] = players[j + 1], players[j]

    write_json(players)


def sort_players_by(criteria):
    players = read_json()
    n = len(players)

    for i in range(n):
        for j in range(0, n - i - 1):
            valor_actual = players[j].get(criteria, 0)
            valor_siguiente = players[j + 1].get(criteria, 0)

            # Burbuja clásica: si el actual es mayor que el siguiente, intercambiar
            if valor_actual > valor_siguiente:
                players[j], players[j + 1] = players[j + 1], players[j]

    write_json(players)