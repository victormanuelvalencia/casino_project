class Queue:
    def __init__(self, initial_data=None):
        """
        Initializes the queue. If initial data is provided, it is converted to a list.
        Otherwise, an empty list is initialized to represent the queue.
        """
        if initial_data is not None:
            self.items = list(initial_data)  # Ensure input is treated as a list
        else:
            self.items = []  # Start with an empty queue

    def enqueue(self, item):
        # Adds an item to the end of the queue.
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.
        Raises an IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        """
        Returns the item at the front of the queue without removing it.
        Returns None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # Returns True if the queue is empty, False otherwise.
        return len(self.items) == 0

    def size(self):
        # Returns the number of elements in the queue.
        return len(self.items)

    def to_list(self):
        # Returns a shallow copy of the queue as a list.
        return self.items.copy()

    def clear(self):
        # Empties all elements from the queue.
        self.items = []
