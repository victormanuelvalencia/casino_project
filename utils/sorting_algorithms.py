# Burbuja, selección, inserción, mezcla
# utils/data_management.py
import json
from utils.file_handler import read_json, write_json


def sort_names_alphabetically(path):
    players = read_json(path)
    n = len(players)

    for i in range(n):
        for j in range(0, n - i - 1):
            nombre_actual = players[j].get("full_name", "").lower()
            nombre_siguiente = players[j + 1].get("full_name", "").lower()
            if nombre_actual > nombre_siguiente:
                # Intercambiar posiciones
                players[j], players[j + 1] = players[j + 1], players[j]

    write_json(path, players)