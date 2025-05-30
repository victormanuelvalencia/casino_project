import random
from itertools import product
from players.player import Player
from utils.file_administration import *


game = 'slot machine'
state = None


def play_slot_machine(player: Player):
    players_data = read_json()
    matriz = [
        ["🍒", "🍊", "🍇"],
        ["🍒", "🍊", "🍇"],
        ["🍒", "🍊", "🍇"]
    ]


    combinaciones = list(product(*matriz))  # Todas las posibles combinaciones
    # print(combinaciones)
    while True:
        try:
            apuesta = float(input(f"Tu balance actual es ${player.get_balance():.2f}. ¿Cuánto deseas apostar?: "))
            if apuesta <= 0:
                print("La apuesta debe ser mayor que cero.")
                continue
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if apuesta > player.get_balance():
            print("No tienes suficiente saldo para esa apuesta.")
            # Guardar lo que se tiene por ahora
            update_player_in_data(player)

            return

        # Ejecutar la apuesta
        player.set_balance(player.get_balance() - apuesta)
        player.set_total_bet(player.get_total_bet() + apuesta)

        resultado = random.choice(combinaciones)
        print("Resultado:", resultado)

        if resultado[0] == resultado[1] == resultado[2]:
            print("¡Ganaste!")
            premio = apuesta * 2  # Por ejemplo, duplicar la apuesta
            player.set_balance(player.get_balance() + premio)
            player.set_games_won(player.get_games_won() + 1)
        else:
            print("Perdiste.")
            player.set_games_lost(player.get_games_lost() + 1)

        seguir = input("¿Deseas jugar otra vez? (s/n): ").strip().lower()
        if seguir != 's':
            break

    # Guardar cambios en el JSON
    update_player_in_data(player)
    print("Gracias por jugar. ¡Hasta la próxima!")

