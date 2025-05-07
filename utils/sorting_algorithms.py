# Burbuja, selección, inserción, mezcla
# utils/data_management.py
import json
from utils.file_administration import read_json, write_json


# Algoritmo de ordenamiento burbuja, pero con los nombres
# Funciona por medio de codigo ASCII
def sort_names_alphabetically():
    players = read_json()
    n = len(players)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Los hacemos minuscla para que no se confunda el codigo entre mayusculas
            # y minusculas
            nombre_actual = players[j].get("full_name", "").lower()
            nombre_siguiente = players[j + 1].get("full_name", "").lower()
            if nombre_actual > nombre_siguiente:
                # Intercambiar posiciones
                players[j], players[j + 1] = players[j + 1], players[j]

    write_json(players)