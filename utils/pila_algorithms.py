class PriorityStack:
    """
    Implements a custom stack data structure with overwrite behavior on push,
    using an internal list and index tracking.

    Attributes:
    - queue: list. Internal list used to store elements.
    - index: int. Points to the current top of the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack with an internal list and sets the top index to -1.
        """
        self.queue = []
        self.index = -1

    def push(self, value):
        """
        Adds a new value to the top of the stack.
        If a value already exists at that position, it is overwritten.

        Parameters:
        - value: any. The value to be added to the stack.

        Returns:
        - None. Modifies the stack in-place.
        """
        self.index += 1
        if self.index < len(self.queue):
            self.queue[self.index] = value
        else:
            self.queue.append(value)

    def pop(self):
        """
        Removes and returns the value at the top of the stack.

        Parameters:
        - None.

        Returns:
        - The value at the top of the stack.

        Raises:
        - IndexError: if the stack is empty.
        """
        if self.index == -1:
            raise IndexError("Pop from empty stack")
        value = self.queue[self.index]
        self.index -= 1
        return value

    def top(self):
        """
        Returns the value at the top of the stack without removing it.

        Parameters:
        - None.

        Returns:
        - The value at the top of the stack.

        Raises:
        - IndexError: if the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("Top from empty stack")
        return self.queue[self.index]

    def isEmpty(self):
        """
        Checks whether the stack is empty.

        Parameters:
        - None.

        Returns:
        - True if the stack is empty, False otherwise.
        """
        return self.index == -1