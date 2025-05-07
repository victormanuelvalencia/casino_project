import random
from itertools import product
from players.player import Player
from utils.file_handler import read_json, write_json

PLAYER_FILE = "data/players.json"


def play_slot_machine(player: Player):
    players_data = read_json(PLAYER_FILE)
    matriz = [
        ["🍒", "🍊", "🍇"],
        ["🍒", "🍊", "🍇"],
        ["🍒", "🍊", "🍇"]
    ]

    combinaciones = list(product(*matriz))  # Todas las posibles combinaciones

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
    print(player)
    print(player.to_dict())
    for idx, data in enumerate(players_data):
        if data["player_id"] == player.get_player_id():
            players_data[idx] = player.to_dict()
            break
    write_json(PLAYER_FILE, players_data)
    print("Gracias por jugar. ¡Hasta la próxima!")

