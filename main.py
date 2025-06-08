from games.blackjack import blackjack
from games.waiting_queue import PlayerQueue
# main.py
from players.player_controller import *
from games.slot_machine import *
from reports.report_generator import *

PLAYER_FILE = "data/players.json"

def player_menu():
    while True:
        print("\n--- Menú de Jugadores ---")
        print("1. Obtener jugador por ID")
        print("6. Buscar jugador por nombre")
        print("2. Crear jugador")
        print("3. Actualizar jugador")
        print("4. Eliminar jugador")
        print("5. Volver al menú principal")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            pId = input("Ingresa el ID del jugador: ")
            get_player_fromId(pId)
        elif choice == "2":
            create_player()
        elif choice == "3":
            update_player()
        elif choice == "4":
            delete_player()
        elif choice == "6":
            pName = input("Ingresa el nombre del jugador: ")
            get_player_fromName(pName)
        elif choice == "5":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")



def game_menu():
    while True:
        print("\n--- Menú de Juegos ---")
        print("1. Jugar tragamonedas")
        print("2. Jugar blackjack")
        print("3. Volver al menú principal")

        choice = input("Selecciona una opción: ").strip()

        if choice == "1":
            queue = PlayerQueue()
            queue.collect_players()
            queue.process_queue(play_slot_machine)
        elif choice == "2":
            queue = PlayerQueue()
            queue.collect_players()
            queue.process_queue(blackjack)
        elif choice == "3":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

def metrics_menu():
    while True:
        print("\n--- Menú de Métricas ---")
        print("1. Show players with best balance")
        print("2. Show history of a player")
        print("3. Show top players")
        print("4. Show players at the bottom")
        print("5. Show more played games")
        print("6. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            ranking_players_in("balance")
        if choice == "2":
            player_id = input("Player's ID: ")
            player = get_player_fromId(player_id)
            if player:
                player.get_history()
        if choice == "3":
            ranking_players_in("games_won")
        if choice == "4":
            ranking_players_in("games_lost")
        elif choice == "6":
            break
        else:
            print("Invalid option. Try again.")

def main_menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Menú de jugadores")
        print("2. Menú de juegos")
        print("3. Métricas de jugadores")
        print("4. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            player_menu()
        elif choice == "2":
            game_menu()
        elif choice == "3":
            metrics_menu()
        elif choice == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main_menu()

