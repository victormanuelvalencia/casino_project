# Clase de pila personalizada (historial)

class Stack:
    def __init__(self, initial_data=None):
        if initial_data is not None:
            self.items = list(initial_data)
        else:
            self.items = []

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

    def show(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            for item in self.items:
                print(item)


