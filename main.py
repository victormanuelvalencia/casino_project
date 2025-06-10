from games.blackjack import blackjack
from games.waiting_queue import PlayerQueue
from controllers.player_controller import *
from games.slot_machine import *
from reports.report_generator import *

PLAYER_FILE = "data/players.json"

def player_menu():
    """
    Displays the Player Management Menu.
    Allows users to:
    1. Retrieve a player by their ID
    2. Search for a player by name
    3. Create a new player
    4. Update an existing player's information
    5. Delete a player
    6. Return to the main menu

    Repeats until the user opts to return.
    """
    while True:
        print("\n--- Player Menu ---")
        print("1. Get player by ID")
        print("2. Search player by name")
        print("3. Create player")
        print("4. Update player")
        print("5. Delete player")
        print("6. Return to main menu")
        choice = input("Select an option: ")

        if choice == "1":
            pId = input("Enter player ID: ")
            get_player_fromId(pId)
        elif choice == "2":
            pName = input("Enter player name: ")
            get_player_fromName(pName)
        elif choice == "3":
            create_player()
        elif choice == "4":
            update_player()
        elif choice == "5":
            delete_player()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

def game_menu():
    """
    Displays the Game Menu.
    Allows users to:
    1. Play the slot machine game
    2. Play blackjack
    3. Return to the main menu

    For games, players are queued before playing.
    Loops until the user chooses to return.
    """
    while True:
        print("\n--- Game Menu ---")
        print("1. Play slot machine")
        print("2. Play blackjack")
        print("3. Return to main menu")

        choice = input("Select an option: ").strip()

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
            print("Invalid option. Please try again.")

def metrics_menu():
    """
    Displays the Player Metrics Menu.
    Provides options to view:
    1. Players with the highest balance
    2. History of a specific player by ID
    3. Top players by games won
    4. Players with the most losses
    5. Most played games (option placeholder)
    6. Return to main menu

    Continuously prompts until exit option is selected.
    """
    while True:
        print("\n--- Metrics Menu ---")
        print("1. Show players with best balance")
        print("2. Show history of a player")
        print("3. Show top players")
        print("4. Show players at the bottom")
        print("5. Show most played games")
        print("6. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            ranking_players_in("balance")
        elif choice == "2":
            player_id = input("Player's ID: ")
            player = get_player_fromId(player_id)
            if player:
                player.get_last_n_history()
        elif choice == "3":
            ranking_players_in("games_won")
        elif choice == "4":
            ranking_players_in("games_lost")
        elif choice == "5":
            ranking_games_in("count")
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

def main_menu():
    """
    Main application menu that orchestrates navigation between
    Player Management, Game Play, and Metrics menus.

    Provides an exit option to terminate the application.
    """
    while True:
        print("\n--- Main Menu ---")
        print("1. Player Menu")
        print("2. Game Menu")
        print("3. Player Metrics")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            player_menu()
        elif choice == "2":
            game_menu()
        elif choice == "3":
            metrics_menu()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()