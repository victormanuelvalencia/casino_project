class PriorityStack:
    def __init__(self):
        # The internal list will serve as our stack structure
        self.queue = []
        # The index keeps track of the current top of the stack
        self.index = -1

    def push(self, value):
        """
        Adds a new value to the top of the stack.
        If the internal list already has an element at the top index, it is overwritten.
        Otherwise, the value is appended to the list.
        """
        self.index += 1
        if self.index < len(self.queue):
            self.queue[self.index] = value
        else:
            self.queue.append(value)

    def pop(self):
        """
        Removes and returns the value at the top of the stack.
        Raises IndexError if the stack is empty.
        """
        if self.index == -1:
            raise IndexError("Pop from empty stack")
        value = self.queue[self.index]
        self.index -= 1
        return value

    def top(self):
        """
        Returns the value at the top of the stack without removing it.
        Raises IndexError if the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("Top from empty stack")
        return self.queue[self.index]

    def isEmpty(self):
        """
        Checks whether the stack is empty.
        Returns True if empty, False otherwise.
        """
        return self.index == -1