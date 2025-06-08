import random
from itertools import product

from controllers.game_controller import get_game_fromName
from utils.file_administration import *
from utils.config import *


def play_slot_machine(player):

    game_data = read_json(GAME_FILE)

    game = get_game_fromName("slot_machine")
    game.increment_count()


    matriz = [
        ["🍒", "🍊", "🍇"],
        ["🍒", "🍊", "🍇"],
        ["🍒", "🍊", "🍇"]
    ]


    combinaciones = list(product(*matriz))  # Todas las posibles combinaciones
    # print(combinaciones)
    while True:
        try:
            bet = float(input(f"Tu balance actual es ${player.get_balance():.2f}. ¿Cuánto deseas apostar?: "))
            if bet <= 0:
                print("La bet debe ser mayor que cero.")
                continue
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if bet > player.get_balance():
            print("No tienes suficiente saldo para esa bet.")
            # Guardar lo que se tiene por ahora
            update_player_in_data(player)

            return


        # Ejecutar la bet
        player.set_history(f'Bet in slot machine: {bet}')
        player.set_balance(player.get_balance() - bet)
        player.set_total_bet(player.get_total_bet() + bet)

        resultado = random.choice(combinaciones)
        print("Resultado:", resultado)

        if resultado[0] == resultado[1] == resultado[2]:
            print("¡Ganaste!")
            earn = bet * 2  # Por ejemplo, duplicar la bet
            player.set_history(f'Won: {earn} in slot machine')
            player.set_balance(player.get_balance() + earn)
            player.set_games_won(player.get_games_won() + 1)
        else:
            print("Perdiste.")
            player.set_history(f'Lose: {bet} in slot machine')
            player.set_games_lost(player.get_games_lost() + 1)

        seguir = input("¿Deseas jugar otra vez? (s/n): ").strip().lower()
        if seguir != 's':
            break

    # Guardar cambios en el JSON
    update_player_in_data(player)
    print("Gracias por jugar. ¡Hasta la próxima!")

