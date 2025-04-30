from players.player import Player
from utils.stack import Stack
from utils.file_handler import read_json, write_json

# Declaramos el archivo donde guardaremos la información de los jugadores
PLAYER_FILE = "data/players.json"

# Función para obtener un jugador por medio de su id
def get_player(player_id):
    # Obtenemos y cargamos la informacion de players.json por medio de la ruta
    players_data = read_json(PLAYER_FILE)

    # Recorremos cada uno de los jugadores
    for data in players_data:
        print(data)
        # Comparamos el player_id del diccionario del jugador en el que estamos con el que
        # estamos buscando por medio del parametro
        if data["player_id"] == player_id:
            player = Player.from_dict(data)
            print(player)  # Usa __str__
            return
    print("Player not found.")


def create_player():
    full_name = input("Full name: ")
    player_id = input("Player ID: ")
    try:
        balance = float(input("Initial balance: "))
    except ValueError:
        print("Balance must be a number.")
        return

    players_data = read_json(PLAYER_FILE)

    if any(p["player_id"] == player_id for p in players_data):
        print("A player with this ID already exists.")
        return

    player = Player(full_name, player_id, balance)
    players_data.append(player.to_dict())
    write_json(PLAYER_FILE, players_data)
    print("Player created successfully.")


def update_player():
    player_id = input("Enter the player ID to update: ")
    players_data = read_json(PLAYER_FILE)

    for index, data in enumerate(players_data):
        if data["player_id"] == player_id:
            player = Player.from_dict(data)

            print(f"Current full name: {player.get_full_name()}")
            new_name = input("New full name (leave blank to keep current): ")
            if new_name:
                player.set_full_name(new_name)

            print(f"Current balance: {player.get_balance()}")
            new_balance = input("New balance (leave blank to keep current): ")
            if new_balance:
                try:
                    player.set_balance(float(new_balance))
                except ValueError:
                    print("Invalid balance. Update aborted.")
                    return

            players_data[index] = player.to_dict()
            write_json(PLAYER_FILE, players_data)
            print("Player updated successfully.")
            return

    print("Player not found.")


def delete_player():
    player_id = input("Enter the player ID to delete: ")
    players_data = read_json(PLAYER_FILE)

    new_data = [p for p in players_data if p["player_id"] != player_id]

    if len(new_data) == len(players_data):
        print("Player not found.")
        return

    write_json(PLAYER_FILE, new_data)
    print("Player deleted successfully.")


