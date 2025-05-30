 # Gestión de cola para mesas populares

from collections import deque

class WaitingQueue:
    def __init__(self):
        self.queue = deque()

    def add_player(self, player_id):
        self.queue.append(player_id)

    def next_player(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def show_queue(self):
        return list(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def players_queue(self):

        while True:
            player_id = input('Ingrese el ID del jugador que se unirá a la mesa:')

            self.add_player(player_id)

            break_point = input('¿Desea seguir agregando jugadores? (y/n)').lower

            if break_point == 'n':
                break

