# Lectura/escritura JSON

import json

from players.player import Player

PLAYER_FILE = "data/players.json"

def read_json():
    with open(PLAYER_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def write_json(data):
    with open(PLAYER_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def update_player_in_data(player):
    """
    Busca al jugador por ID y actualiza sus datos en el archivo JSON.
    Esta función puede ser utilizada en múltiples juegos o módulos.
    """
    players_data = read_json()

    # Buscar al jugador por su player_id y actualizar sus datos
    for idx, data in enumerate(players_data):
        if data["player_id"] == player.get_player_id():
            players_data[idx] = player.to_dict()
            break

    # Guardar los cambios
    write_json(players_data)
