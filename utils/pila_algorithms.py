class PriorityStack:
    def __init__(self):
        self.queue = []  # El arreglo actuará como nuestra pila
        self.index = -1  # El índice para manejar el tope de la pila

    def push(self, value):
        self.index += 1
        if self.index < len(self.queue):
            self.queue[self.index] = value
        else:
            self.queue.append(value)

    def pop(self):
        if self.index == -1:
            raise IndexError("Pop from empty stack")
        value = self.queue[self.index]
        self.index -= 1
        return value

    def top(self):
        if self.isEmpty():
            raise IndexError("Top from empty stack")
        return self.queue[self.index]

    def isEmpty(self):
        return self.index == -1
