# Lectura/escritura JSON

import json

PLAYER_FILE = "data/players.json"

def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def write_json(path, data):
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
    write_json(PLAYER_FILE, players_data)
