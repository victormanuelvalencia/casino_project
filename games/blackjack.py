import random

from players.player import Player
from utils.file_administration import *


# Calcula el valor de una sola carta
def calculate_hand_value(card, hand):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        # Si al sumar 11 te pasas, el As vale 1
        return 11 if hand + 11 <= 21 else 1
    else:
        return int(card)


# Reparte una carta
def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Juego principal
def blackjack(player: Player, hand=0, turn=0, bet=0):

    """
    Para el turno 0 debemos mostrar y preguntar por consola cuanto se
    desea apostar
    """
    if turn == 0:

        try:
            bet = float(input(f'Your actual balance is: {player.get_balance()}. How much do you want to bet? '))
            if bet <= 0:
                print("La apuesta debe ser mayor que cero.")
                return blackjack(player, hand, turn, bet)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            return blackjack(player, hand, turn, bet)

        # Validar si tiene el dinero suficiente para realizar la apuesta
        if bet > player.get_balance():
            print("You don't have enought balance to do this bet.")
            return False

        # Insertamos el dinero y lo apostado resultante
        player.set_history(f'Apostó: {bet}')
        player.set_balance(player.get_balance() - bet)
        player.set_total_bet(player.get_total_bet() + bet)
        # Primer turno: se reparten dos cartas
        card1 = deal_card()
        card2 = deal_card()
        # Calcular su valor
        value1 = calculate_hand_value(card1, hand)
        value2 = calculate_hand_value(card2, hand)
        hand = value1 + value2
        print(f"Start: card {card1}, value: ({value1}), card {card2}, value: ({value2})")

        # Llamada recursiva donde enviamos la mano, la apuesta y aumentamos el turno
        return blackjack(player, hand, turn + 1, bet)


    print(f"Your current hand value: {hand}")
    # Preguntamos si se quiere sacar otra carta
    choice = input("Do you want another card? (y/n): ").lower()
    # Cuando quiera sacarla
    if choice == 'y':
        # Sacar la carta
        card = deal_card()
        # Calcular su valor
        value = calculate_hand_value(card, hand)
        print(f"Dealt card: {card}, value: {value}")
        # Sumarlo a la mano
        hand += value
        # Y si la mano se pasa de 21, pierde y se incrementa el contador games_lost
        if hand > 21:
            player.set_games_lost(player.get_games_lost() + 1)
            player.set_history(f'Perdió: {bet}')
            print("You went over 21. You lose.")
            update_player_in_data(player)
            return False
        # De lo contrario, que continue con la llamada recursiva, con la mano actual y
        # se incrementa el turno
        return blackjack(player, hand, turn + 1, bet)

    # Si no se quiere continuar, entonces se calcula la ganancia, se incrementa el contador
    # games_won y se actualiza la info

    else:
        earn = calculate_bet(bet, hand)
        player.set_balance(player.get_balance() + earn)
        player.set_games_won(player.get_games_won() + 1)
        player.set_history(f'Gano: {earn}')
        print(f'You retired. You won {calculate_bet(bet, hand)}, you have {player.get_balance()}')
        update_player_in_data(player)




def calculate_bet(bet, hand):
    return int(((bet/21) * hand) + bet)


