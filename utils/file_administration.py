# Lectura/escritura JSON

import json
from config import *


def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def write_json(data, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def update_player_in_data(player):
    """
    Busca al jugador por ID y actualiza sus datos en el archivo JSON.
    Esta función puede ser utilizada en múltiples juegos o módulos.
    """
    players_data = read_json(PLAYER_FILE)

    # Buscar al jugador por su player_id y actualizar sus datos
    for idx, data in enumerate(players_data):
        if data["player_id"] == player.get_player_id():
            players_data[idx] = player.to_dict()
            break

    # Guardar los cambios
    write_json(players_data, PLAYER_FILE)

def update_game_in_data(game):
    """
    Busca un juego por su nombre y actualiza sus datos en el archivo JSON.
    Esta función puede ser utilizada en múltiples módulos que gestionen juegos.
    """
    games_data = read_json(GAME_FILE)

    # Buscar el juego por su game_name y actualizar sus datos
    for idx, data in enumerate(games_data):
        if data["game_name"] == game.get_game_name():
            games_data[idx] = game.to_dict()
            break

    # Guardar los cambios
    write_json(games_data, GAME_FILE)
