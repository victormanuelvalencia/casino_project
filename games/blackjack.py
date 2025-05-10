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
def blackjack(player: Player, hand=0, turn=0):


    if turn == 0:
        print(f'Tu dinero total es: {player.get_balance()}')
        bet = int(input('Cuando quieres apostar?'))

        player.set_balance(player.get_balance() - bet)
        player.set_total_bet(player.get_total_bet() + bet)

        # Primer turno: repartir dos cartas
        card1 = deal_card()
        card2 = deal_card()
        value1 = calculate_hand_value(card1, hand)
        value2 = calculate_hand_value(card2, hand)
        hand = value1 + value2
        print(f"Start: {card1}, value: ({value1}), {card2}, value: ({value2})")
        return blackjack(hand, turn + 1)


    print(f"Your current hand value: {hand}")
    choice = input("Do you want another card? (y/n): ").lower()
    if choice == 'y':
        card = deal_card()
        value = calculate_hand_value(card, hand)
        print(f"Dealt card: {card}, value: {value}")
        hand += value
        if hand > 21:
            print("You went over 21. You lose.")
            player.set_games_lost(player.get_games_lost() - 1)
            update_player_in_data(player)
            return False
        return blackjack(hand, turn + 1)

    else:
        player.set_balance(calculate_bet(bet, hand))
        player.set_games_won(player.get_games_won() + 1)
        update_player_in_data(player)

# Ejecutar el juego
print("Result:", blackjack())


def calculate_bet(bet, hand):
    return (bet/21) * hand


