from players.player import Player
from utils.sorting_algorithms import *
from utils.stack import Stack
from utils.file_handler import *

# Declaramos el archivo donde guardaremos la información de los jugadores
PLAYER_FILE = "data/players.json"

# Función para obtener un jugador por medio de su id
def get_player_fromId(player_id):
    # Obtenemos y cargamos la informacion de players.json por medio de la ruta
    players_data = read_json(PLAYER_FILE)

    # Recorremos cada uno de los jugadores
    for data in players_data:
       # print(data)
        # Comparamos el player_id del diccionario del jugador en el que estamos con el que
        # estamos buscando por medio del parametro
        if data["player_id"] == player_id:
            player = Player.from_dict(data) # Cuando se encuentre, convertimos de diccionario
                                            # a un objeto de la clase Player
            return print(player) # Imprimimos por consola el objeto resultante
    print("Player not found.") # Si termina el ciclo sin hacer un retorno, entonces no existe el usuario


# Función para crear un jugador
def create_player():
    # Obtenemos la informacion del archivo players.json
    players_data = read_json(PLAYER_FILE)

    full_name = input("Full name: ")
    player_id = input("Player ID: ")

    # Buscamos si existe un jugador con este id
    for p in players_data:
        if p["player_id"] == player_id:
            return print("A player with this ID already exists.")

    try:
        balance = float(input("Initial balance: "))
    except ValueError:
        return print("Balance must be a number.")

    # Instancia de Player con los inputs anteriores
    player = Player(full_name, player_id, balance)
    # Lo agregamos a la lista del archivo players.json la información en forma de diccionario
    # con to_dict()
    players_data.append(player.to_dict())
    # Y sobrescribo el archivo
    # Puede cambiar con una funcion de actualizacion
    write_json(PLAYER_FILE, players_data)
    # Ordenamos los nombres alfabeticamente
    sort_names_alphabetically(PLAYER_FILE)

    print("Player created successfully.")


def update_player():
    players_data = read_json(PLAYER_FILE)
    player_id = input("Enter the player ID to update: ")

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
                    return print("Invalid balance. Update aborted.")

            # En la posicion del json escribimos la informacion del jugador
            players_data[index] = player.to_dict()
            # Escribimos los datos del jugador actualizados
            write_json(PLAYER_FILE, players_data)
            # Re organizamos alfabeticamente
            sort_names_alphabetically(PLAYER_FILE)
            print("Player updated successfully.")
            return

    print("Player not found.")


def delete_player():
    player_id = input("Enter the player ID to delete: ")
    players_data = read_json(PLAYER_FILE)

   # new_data = [p for p in players_data if p["player_id"] != player_id]

    new_data = []
    for p in players_data:
        if p["player_id"] != player_id:
            new_data.append(p)

    if len(new_data) == len(players_data):
        return print("Player not found.")

    write_json(PLAYER_FILE, new_data)
    print("Player deleted successfully.")


