import random
from itertools import product

from controllers.game_controller import get_game_fromName
from utils.file_administration import *
from utils.config import *

def play_slot_machine(player):
    """
    Runs a slot machine session for the given player.
    Handles betting, random symbol generation, win/loss evaluation, and updates the player data.

    Parameters:
    - player: Player object participating in the game. Must support methods for balance management,
              game history tracking, and statistics updates.

    Returns:
    - None when the game ends. Updates are persisted automatically.
    """
    
    # Load game data and increment the play count
    game = get_game_fromName("slot_machine")
    game.increment_count()

    # Define the slot machine matrix (3 columns of symbols)
    matrix = [
        ["🍒", "🍊", "🍇"],
        ["🍒", "🍊", "🍇"],
        ["🍒", "🍊", "🍇"]
    ]

    # Generate all possible combinations (one symbol from each column)
    combinations = list(product(*matrix))

    while True:
        # Prompt the player for a betting amount
        try:
            bet = float(input(f"Your current balance is ${player.get_balance():.2f}. How much do you want to bet?: "))
            if bet <= 0:
                print("The bet must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Ensure the player has enough balance
        if bet > player.get_balance():
            print("Insufficient balance to place this bet.")
            update_player_in_data(player)
            return

        # Register the bet in the player's history and adjust balance
        player.set_history(f'Bet in slot machine: {bet}')
        player.set_balance(player.get_balance() - bet)
        player.set_total_bet(player.get_total_bet() + bet)

        # Randomly select a result from the possible combinations
        result = random.choice(combinations)
        print("Result:", result)

        # Check if all three symbols match
        if result[0] == result[1] == result[2]:
            print("You won!")
            earnings = bet * 2  # Double the bet as a prize
            player.set_history(f'Won: {earnings} in slot machine')
            player.set_balance(player.get_balance() + earnings)
            player.set_games_won(player.get_games_won() + 1)
            update_game_in_data(game)
        else:
            print("You lost.")
            player.set_history(f'Lost: {bet} in slot machine')
            player.set_games_lost(player.get_games_lost() + 1)
            update_game_in_data(game)
        # Ask the player if they want to play again
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            break

    # Persist player's updated information
    update_player_in_data(player)
    print("Thanks for playing. See you next time!")