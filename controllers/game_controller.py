from utils.config import GAME_FILE
from utils.file_administration import read_json
from utils.sorting_algorithms import sort_elements_by
from models.game import Game

def get_game_fromName(game_name):
    sort_elements_by("game_name", GAME_FILE)
    # Obtenemos y cargamos la informacion de games.json por medio de la ruta
    games_data = read_json(GAME_FILE)

    # Recorremos cada uno de los jugadores
    for data in games_data:
       # print(data)
        # Comparamos el nombre del diccionario del jugador en el que estamos con el que
        # estamos buscando por medio del parametro
        if data["game_name"] == game_name:
            game = Game.from_dict(data) # Cuando se encuentre, convertimos de diccionario
            # Imprimimos por consola el objeto resultante
            print(game)
            return game
    # print("game not found.") # Si termina el ciclo sin hacer un retorno, entonces no existe el usuario
    print(-1)
    return False