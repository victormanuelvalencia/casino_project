from players.player import Player
from utils.sorting_algorithms import *
from utils.stack import Stack
from utils.file_administration import *


# Busqueda por nombre (lineal)
def get_player_fromName(player_full_name):
    sort_ids_alphabetically()
    # Obtenemos y cargamos la informacion de players.json por medio de la ruta
    players_data = read_json()

    # Recorremos cada uno de los jugadores
    for data in players_data:
       # print(data)
        # Comparamos el nombre del diccionario del jugador en el que estamos con el que
        # estamos buscando por medio del parametro
        if data["full_name"] == player_full_name:
            player = Player.from_dict(data) # Cuando se encuentre, convertimos de diccionario
            # Imprimimos por consola el objeto resultante
            print(player)
            return player
    # print("Player not found.") # Si termina el ciclo sin hacer un retorno, entonces no existe el usuario
    return False

# Busqueda por nombre (binaria)
def get_player_fromId(player_id):
    sort_ids_alphabetically()
    # Obtenemos y cargamos la informacion de players.json por medio de la ruta
    players_data = read_json()

    n = len(players_data)

    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        mid_name = players_data[mid]["player_id"].lower()

        if mid_name == player_id.lower():
            player = Player.from_dict(players_data[mid])
            print(player)
            return player
        elif mid_name > player_id.lower():
            right = mid - 1
        else:
            left = mid + 1

    return False  # No encontrado

# Función para crear un jugador
def create_player():
    # Obtenemos la informacion del archivo players.json
    players_data = read_json()

    full_name = input("Full name: ")
    player_id = input("Player ID: ")

    # Buscamos si existe un jugador con este id
    if get_player_fromId(player_id):
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
    write_json(players_data)
    # Ordenamos los nombres alfabeticamente
    sort_ids_alphabetically()

    print("Player created successfully.")


def update_player():
    players_data = read_json()
    player_id = input("Enter the player ID to update: ")

    player = get_player_fromId(player_id)
    if not player:
        return

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

    for index, data in enumerate(players_data):
        if data["player_id"] == player_id:
            players_data[index] = player.to_dict()
            write_json(players_data)
            sort_ids_alphabetically()
            print("Player updated successfully.")
            return
    print("Player not found.")
    return



def delete_player():
    player_id = input("Enter the player ID to delete: ")
    players_data = read_json()

   # new_data = [p for p in players_data if p["player_id"] != player_id]

    copy_data = []
    for p in players_data:
        if p["player_id"] != player_id:
            copy_data.append(p)

    if len(copy_data) == len(players_data):
        return print("Player not found.")

    write_json(copy_data)
    print("Player deleted successfully.")

def add_history(player, action: str):
    #timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    player.history.push(f"{action}")


