# Clase de pila personalizada (historial)

class Stack:
    def __init__(self, initial_data=None):
        self.items = initial_data if initial_data is not None else []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def to_list(self):
        return self.items.copy()

    def clear(self):
        self.items = []

