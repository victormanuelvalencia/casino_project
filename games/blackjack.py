import random
from controllers.game_controller import get_game_fromName
from utils.file_administration import *

# Calculates the value of a single card based on blackjack rules
def calculate_hand_value(card, hand):
    """
    Returns the value of a given card based on current hand value.

    Parameters:
    - card: string representing the drawn card ('2' to '10', 'J', 'Q', 'K', 'A').
    - hand: current value of the player's hand.

    Returns:
    - Integer value of the card according to blackjack rules.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        # Ace is 11 if it doesn't bust the hand, otherwise it's 1
        return 11 if hand + 11 <= 21 else 1
    else:
        return int(card)

# Returns a randomly selected card from a standard blackjack deck
def deal_card():
    """
    Selects a random card from a predefined list.

    Returns:
    - A string representing the card drawn.
    """
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Main function for the blackjack game logic
def blackjack(player, hand=0, turn=0, bet=0):
    """
    Runs a blackjack session for the given player.
    Handles betting, card drawing, turn management, and updates the player data.

    Parameters:
    - player: Player object participating in the game.
    - hand: current hand value (default is 0).
    - turn: turn number (default is 0; first turn).
    - bet: amount bet by the player (default is 0).

    Returns:
    - False if the player loses or exits due to insufficient funds.
    - None when the game ends successfully.
    """

    # Get the blackjack game object and increment its play count
    game = get_game_fromName("blackjack")
    game.increment_count()

    if turn == 0:
        # First turn: prompt for betting amount
        try:
            bet = float(input(f'Your current balance is: {player.get_balance()}. How much do you want to bet? '))
            if bet <= 0:
                print("The bet must be greater than zero.")
                return blackjack(player, hand, turn, bet)
        except ValueError:
            print("Please enter a valid number.")
            return blackjack(player, hand, turn, bet)

        # Verify that the player has enough balance
        if bet > player.get_balance():
            print("You don't have enough balance to place this bet.")
            return False

        # Deduct the bet from player's balance and update history
        player.set_history(f'Bet in blackjack: {bet}')
        player.set_balance(player.get_balance() - bet)
        player.set_total_bet(player.get_total_bet() + bet)

        # Deal the initial two cards
        card1 = deal_card()
        card2 = deal_card()
        value1 = calculate_hand_value(card1, hand)
        value2 = calculate_hand_value(card2, hand)
        hand = value1 + value2

        print(f"Start: card {card1} (value: {value1}), card {card2} (value: {value2})")

        # Recursively proceed to the next turn
        return blackjack(player, hand, turn + 1, bet)

    # Display the current hand value to the player
    print(f"Your current hand value: {hand}")

    # Ask whether the player wants another card
    choice = input("Do you want another card? (y/n): ").lower()

    if choice == 'y':
        # Player draws another card
        card = deal_card()
        value = calculate_hand_value(card, hand)
        print(f"Dealt card: {card}, value: {value}")
        hand += value

        # If the hand goes over 21, the player loses
        if hand > 21:
            print("You went over 21. You lose.")
            player.set_games_lost(player.get_games_lost() + 1)
            player.set_history(f'Lost: {bet} in blackjack')
            update_player_in_data(player)
            return False

        # Continue the game recursively
        return blackjack(player, hand, turn + 1, bet)

    else:
        # Player decides to stop; calculate earnings
        earn = calculate_bet(bet, hand)
        print(f'You stopped. You won {earn}, your new balance is {player.get_balance() + earn}')
        player.set_balance(player.get_balance() + earn)
        player.set_games_won(player.get_games_won() + 1)
        player.set_history(f'Won: {earn} in blackjack')
        update_player_in_data(player)

# Calculates the final earnings based on hand value and original bet
def calculate_bet(bet, hand):
    """
    Computes the amount earned based on how close the hand is to 21.

    Parameters:
    - bet: the original amount bet by the player.
    - hand: the final value of the player's hand.

    Returns:
    - The calculated earnings as an integer.
    """
    return int(((bet / 21) * hand) + bet)