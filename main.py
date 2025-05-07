# Punto de entrada del programa
"""
from players.player_controller2 import get_player_fromId, create_player, update_player, delete_player

def main_menu():
    while True:
        print("\n--- Player Controller Menu ---")
        print("1. Get player from id")
        print("2. Create player")
        print("3. Update player")
        print("4. Delete player")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            pid = input("Enter player ID: ")
            get_player_fromId(pid)
        elif choice == "2":
            create_player()
        elif choice == "3":
            update_player()
        elif choice == "4":
            delete_player()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
"""
# main.py
from players.player_controller2 import *
from games.slot_machine import *
from utils.file_administration import *


PLAYER_FILE = "data/players.json"

def player_menu():
    while True:
        print("\n--- Menú de Jugadores ---")
        print("1. Obtener jugador por ID")
        print("2. Crear jugador")
        print("3. Actualizar jugador")
        print("4. Eliminar jugador")
        print("5. Volver al menú principal")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            pid = input("Ingresa el ID del jugador: ")
            get_player_fromId(pid)
        elif choice == "2":
            create_player()
        elif choice == "3":
            update_player()
        elif choice == "4":
            delete_player()
        elif choice == "5":
            break
        else:
            print("Opción inválida. Intenta nuevamente.")



def game_menu():
    while True:
        print("\n--- Menú de Juegos ---")
        print("1. Jugar tragamonedas")
        print("2. Volver al menú principal")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            jugador = player_selection()
            if jugador:
                play_slot_machine(jugador)
        elif choice == "2":
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
            jugador = player_selection()
            if jugador:
                print("\nHistorial:")
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

