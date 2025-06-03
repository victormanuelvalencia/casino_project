from games.blackjack import blackjack
from games.waiting_queue import PlayerQueue
# main.py
from players.player_controller import *
from games.slot_machine import *



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
        print("1. Ver historial de un jugador")
        print("2. Volver al menú principal")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            jugador = get_player_fromId()
            if jugador:
                print("\nHistorical:")
                for entry in jugador.history:
                    print(entry)
                print(f"\nTotal apostado: ${jugador.total_bet}")
                print(f"Juegos ganados: {jugador.games_won}")
                print(f"Juegos perdidos: {jugador.games_lost}")
        elif choice == "2":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

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

