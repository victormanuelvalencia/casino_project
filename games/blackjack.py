import random

from controllers.game_controller import get_game_fromName
from utils.file_administration import *

# Calculates the value of a single card according to blackjack rules
def calculate_hand_value(card, hand):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        # If adding 11 exceeds 21, the Ace counts as 1; otherwise, it counts as 11
        return 11 if hand + 11 <= 21 else 1
    else:
        return int(card)

# Returns a random card from the deck
def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Main blackjack game function
def blackjack(player, hand=0, turn=0, bet=0):
    """
    Executes a blackjack session for the given player.
    Handles the full game flow: placing bets, turns, drawing cards, and updating player status.
    
    Parameters:
    - player: Player object representing the current player.
    - hand: current hand value.
    - turn: turn number (0 is the initial turn).
    - bet: current bet amount.
    """

    # Retrieve the "blackjack" game and increment its play count
    game = get_game_fromName("blackjack")
    game.increment_count()

    if turn == 0:
        # First turn: ask the player how much they want to bet
        try:
            bet = float(input(f'Your current balance is: {player.get_balance()}. How much do you want to bet? '))
            if bet <= 0:
                print("The bet must be greater than zero.")
                return blackjack(player, hand, turn, bet)
        except ValueError:
            print("Please enter a valid number.")
            return blackjack(player, hand, turn, bet)

        # Check if the player has enough balance
        if bet > player.get_balance():
            print("You don't have enough balance to place this bet.")
            return False

        # Update player's history and balance
        player.set_history(f'Bet in blackjack: {bet}')
        player.set_balance(player.get_balance() - bet)
        player.set_total_bet(player.get_total_bet() + bet)

        # Deal two initial cards
        card1 = deal_card()
        card2 = deal_card()
        value1 = calculate_hand_value(card1, hand)
        value2 = calculate_hand_value(card2, hand)
        hand = value1 + value2

        print(f"Start: card {card1}, value: ({value1}), card {card2}, value: ({value2})")

        # Recursive call to proceed to the next turn
        return blackjack(player, hand, turn + 1, bet)

    # Show the current value of the hand
    print(f"Your current hand value: {hand}")

    # Ask the player if they want another card
    choice = input("Do you want another card? (y/n): ").lower()

    if choice == 'y':
        # If yes, deal a new card and calculate its value
        card = deal_card()
        value = calculate_hand_value(card, hand)
        print(f"Dealt card: {card}, value: {value}")
        hand += value

        # If the hand exceeds 21, the player loses
        if hand > 21:
            print("You went over 21. You lose.")
            player.set_games_lost(player.get_games_lost() + 1)
            player.set_history(f'Lost: {bet} in blackjack')
            update_player_in_data(player)
            return False

        # Otherwise, continue the game with the updated hand
        return blackjack(player, hand, turn + 1, bet)

    else:
        # If the player stops, calculate the earnings and update the player
        earn = calculate_bet(bet, hand)
        print(f'You stopped. You won {earn}, your new balance is {player.get_balance() + earn}')
        player.set_balance(player.get_balance() + earn)
        player.set_games_won(player.get_games_won() + 1)
        player.set_history(f'Won: {earn} in blackjack')
        update_player_in_data(player)

# Calculates the final gain based on hand value and bet amount
def calculate_bet(bet, hand):
    return int(((bet / 21) * hand) + bet)