from utils.queue import Queue
from players.player import Player
from players.player_controller import get_player_fromId


class PlayerQueue(Queue):
    def collect_players(self):
        """Recolecta los IDs de los jugadores mediante input"""
        print("\n--- Agregar Jugadores a la Cola ---")
        print("Ingrese los IDs de los jugadores (uno por línea)")
        print("Escriba 'fin' para terminar\n")

        while True:
            player_id = input("ID del jugador: ").strip()

            if player_id.lower() == 'fin':
                if self.is_empty():
                    print("¡Debe agregar al menos un jugador!")
                    continue
                break

            if not player_id:
                print("ID no puede estar vacío")
                continue

            # Verificar si el jugador existe
            player = get_player_fromId(player_id)
            if not player:
                print(f"¡Jugador con ID {player_id} no encontrado!")
                continue

            self.enqueue(player)  # Almacenamos el objeto Player directamente
            print(f"Jugador {player_id} agregado. Total en cola: {self.size()}")

    def process_queue(self, game_function):
        """Procesa la cola de jugadores para un juego específico"""
        print("\n--- Procesando Cola de Jugadores ---")

        while not self.is_empty():
            player = self.dequeue()

            print(f"\n>>> Turno de {player.get_id()} <<<")
            game_function(player)

            if not self.is_empty():
                input("\nPresione Enter para pasar al siguiente jugador...")

        print("\nTodos los jugadores han completado su turno.")