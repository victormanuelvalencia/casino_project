class Stack:
    def __init__(self, initial_data=None):
        """
        Initializes the stack.
        If initial_data is provided, converts it to a list to populate the stack.
        Otherwise, initializes an empty stack.
        """
        if initial_data is not None:
            self.items = list(initial_data)
        else:
            self.items = []

    def push(self, item):
        """
        Adds an item to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def top(self):
        """
        Returns the top item without removing it.
        Returns None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """
        Checks if the stack is empty.
        Returns True if empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of items currently in the stack.
        """
        return len(self.items)

    def to_list(self):
        """
        Returns a shallow copy of the stack's contents as a list.
        """
        return self.items.copy()

    def clear(self):
        """
        Empties the stack by removing all items.
        """
        self.items = []

    def show(self):
        """
        Prints all items in the stack from bottom to top.
        Informs if the stack is empty.
        """
        if self.is_empty():
            print("The stack is empty.")
        else:
            for item in self.items:
                print(item)