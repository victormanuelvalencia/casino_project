from utils.queue import Queue
from controllers.player_controller import get_player_fromId

class PlayerQueue(Queue):
    def collect_players(self):
        """
        Collects players by their IDs via user input and enqueues them.
        Ensures that only existing players are added to the queue.

        Parameters:
        - None. This method relies on user input.

        Returns:
        - None. Players are added to the queue as side effects.
        """

        print("\n--- Add Players to the Queue ---")
        print("Enter the player IDs (one per line).")
        print("Type 'fin' to finish.\n")

        while True:
            player_id = input("Player ID: ")

            # Terminate input if user types 'fin'
            if player_id.lower() == 'fin':
                if self.is_empty():
                    print("You must add at least one player!")
                    continue
                break

            # Validate that input is not empty
            if not player_id:
                print("ID cannot be empty.")
                continue

            # Verify player existence
            player = get_player_fromId(player_id)
            if not player:
                print(f"No player found with ID: {player_id}")
                continue

            # Enqueue the player object directly
            self.enqueue(player)
            print(f"Player {player_id} added. Players in queue: {self.size()}")

    def process_queue(self, game_function):
        """
        Processes the queue by executing the provided game function
        for each player in FIFO order.

        Parameters:
        - game_function: Function to be executed for each player in the queue.
                         Must accept a single argument of type Player.

        Returns:
        - None. The function is applied to each player and the queue is emptied as a result.
        """

        print("\n--- Processing Player Queue ---")

        while not self.is_empty():
            player = self.dequeue()

            print(f"\n>>> {player.get_full_name()} ({player.get_player_id()})'s Turn <<<")
            game_function(player)

            if not self.is_empty():
                input("\nPress Enter to continue to the next player...")

        print("\nAll players have completed their turns.")