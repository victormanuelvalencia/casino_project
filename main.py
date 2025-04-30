# Punto de entrada del programa

from players.player_controller2 import get_player, create_player, update_player, delete_player

def main_menu():
    while True:
        print("\n--- Player Controller Menu ---")
        print("1. Get player")
        print("2. Create player")
        print("3. Update player")
        print("4. Delete player")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            pid = input("Enter player ID: ")
            get_player(pid)
        elif choice == "2":
            create_player()
        elif choice == "3":
            update_player()
        elif choice == "4":
            delete_player()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
