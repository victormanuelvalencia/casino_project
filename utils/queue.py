class Queue:
    def __init__(self, initial_data=None):
        if initial_data is not None:
            self.items = list(initial_data)  # Convertimos a lista por si acaso
        else:
            self.items = []  # Lista vacía si no se proporciona dato inicial

    def enqueue(self, item):
        # Añade un elemento al final de la cola
        self.items.append(item)

    def dequeue(self):
        # Elimina y devuelve el primer elemento de la cola
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)  # Elimina el primer elemento

    def front(self):
        # Devuelve el primer elemento sin eliminarlo
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # Comprueba si la cola está vacía
        return len(self.items) == 0

    def size(self):
        # Devuelve el tamaño de la cola
        return len(self.items)

    def to_list(self):
        # Devuelve una copia de la cola como lista
        return self.items.copy()

    def clear(self):
        # Vacía la cola
        self.items = []