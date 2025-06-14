from models.player import Player
from utils.sorting_algorithms import *
from utils.file_administration import *
from utils.config import PLAYER_FILE

# Linear search for a player by full name
def get_player_fromName(player_full_name):
    """
    Searches for a player by their full name using linear search.

    Parameters:
    - player_full_name (str): The full name of the player to search for.

    Returns:
    - Player: The matching Player object if found.
    - False: If no player with the given name is found.
    """

    # Sort players by their full name before searching
    sort_elements_by_bubble("full_name", PLAYER_FILE)

    # Load player data from players.json
    players_data = read_json(PLAYER_FILE)

    # Iterate through the list of players
    for data in players_data:
        # Compare current player's name with the requested name
        if data["full_name"] == player_full_name:
            # Convert the matching dictionary into a Player object
            player = Player.from_dict(data)
            print(player)  # Debug: print the resulting Player object
            return player

    # If no match is found, print -1 and return False
    # print(-1)
    return False

# Binary search for a player by player_id
def get_player_fromId(player_id):
    """
    Searches for a player by their ID using binary search.
    The list is sorted by ID before performing the search.

    Parameters:
    - player_id (str): The unique identifier of the player to search for.

    Returns:
    - Player: The matching Player object if found.
    - False: If no player with the given ID is found.
    """

    # Sort players by their ID before performing binary search
    sort_elements_by_bubble("player_id", PLAYER_FILE)

    # Load player data from players.json
    players_data = read_json(PLAYER_FILE)

    # Initialize binary search pointers
    left = 0
    right = len(players_data) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_id = players_data[mid]["player_id"].lower()

        if mid_id == player_id.lower():
            # Match found, convert to Player object and return
            player = Player.from_dict(players_data[mid])
            print(player)
            return player
        elif mid_id > player_id.lower():
            right = mid - 1
        else:
            left = mid + 1

    # No match found
    # print(-1)
    return False

# Function to create a new player
def create_player():
    """
    Creates a new player based on input provided by the user.

    Parameters:
    - None directly. Prompts the user for full name, ID, and initial balance.

    Flow:
    - Checks for ID duplication.
    - Validates the initial balance.
    - Creates and stores the new player in the JSON file.

    Returns:
    - None: Outputs status messages to the console.
    """

    # Load existing player data
    players_data = read_json(PLAYER_FILE)

    # Gather input from user
    full_name = input("Full name: ")
    player_id = input("Player ID: ")

    # Check if a player with the same ID already exists
    if get_player_fromId(player_id):
        return print("A player with this ID already exists.")

    try:
        balance = float(input("Initial balance: "))
    except ValueError:
        return print("Balance must be a number.")

    # Create a new Player instance
    player = Player(full_name, player_id, balance)

    # Append new player data to the list
    players_data.append(player.to_dict())

    # Save updated data back to the JSON file
    write_json(players_data, PLAYER_FILE)

    # Sort players by ID to maintain order
    #sort_ids_alphabetically()

    print("Player created successfully.")

# Function to update an existing player
def update_player():
    """
    Updates an existing player's full name and/or balance.

    Parameters:
    - None directly. Prompts the user for the player ID and new data.

    Flow:
    - Retrieves the player by ID.
    - Allows the user to update the name and balance (optional).
    - Saves the updated data back to the file.

    Returns:
    - None: Outputs success or failure messages to the console.
    """

    # Load current player data
    players_data = read_json(PLAYER_FILE)
    player_id = input("Enter the player ID to update: ")

    # Search for the player by ID
    player = get_player_fromId(player_id)
    if not player:
        return

    # Prompt for new full name
    print(f"Current full name: {player.get_full_name()}")
    new_name = input("New full name (leave blank to keep current): ")
    if new_name:
        player.set_full_name(new_name)

    # Prompt for new balance
    print(f"Current balance: {player.get_balance()}")
    new_balance = input("New balance (leave blank to keep current): ")
    if new_balance:
        try:
            player.set_balance(float(new_balance))
        except ValueError:
            return print("Invalid balance. Update aborted.")

    # Update the player's entry in the data list
    for index, data in enumerate(players_data):
        if data["player_id"] == player_id:
            players_data[index] = player.to_dict()
            write_json(players_data, PLAYER_FILE)
            #sort_ids_alphabetically()
            print("Player updated successfully.")
            return

    print("Player not found.")
    return

# Function to delete a player by ID
def delete_player():
    """
    Deletes a player from the system by their ID.

    Parameters:
    - None directly. Prompts the user for the player ID to delete.

    Flow:
    - Filters out the player with the matching ID.
    - Updates the JSON file if the player is found and removed.
    - Notifies the user if the player was not found.

    Returns:
    - None: Outputs appropriate status messages to the console.
    """

    player_id = input("Enter the player ID to delete: ")
    players_data = read_json(PLAYER_FILE)

    # Create a filtered list excluding the player to delete
    copy_data = []
    for p in players_data:
        if p["player_id"] != player_id:
            copy_data.append(p)

    # If no player was removed, show not found message
    if len(copy_data) == len(players_data):
        return print("Player not found.")

    # Save the updated list back to the file
    write_json(copy_data, PLAYER_FILE)
    print("Player deleted successfully.")