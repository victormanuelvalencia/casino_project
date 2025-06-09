class Queue:
    """
    Implements a basic First-In-First-Out (FIFO) queue structure
    using a Python list as the underlying container.

    Attributes:
    - items: list. Stores the elements of the queue.
    """

    def __init__(self, initial_data=None):
        """
        Initializes the queue. If initial data is provided, it is converted to a list.
        Otherwise, an empty list is initialized.

        Parameters:
        - initial_data: iterable (optional). Initial elements to populate the queue.

        Returns:
        - None.
        """
        if initial_data is not None:
            self.items = list(initial_data)
        else:
            self.items = []

    def enqueue(self, item):
        """
        Adds an item to the end (rear) of the queue.

        Parameters:
        - item: any. The element to add to the queue.

        Returns:
        - None.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.

        Parameters:
        - None.

        Returns:
        - The element at the front of the queue.

        Raises:
        - IndexError: if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        """
        Returns the item at the front of the queue without removing it.

        Parameters:
        - None.

        Returns:
        - The element at the front of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """
        Checks whether the queue is empty.

        Parameters:
        - None.

        Returns:
        - True if the queue has no elements, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of elements currently in the queue.

        Parameters:
        - None.

        Returns:
        - Integer count of elements in the queue.
        """
        return len(self.items)

    def to_list(self):
        """
        Returns a shallow copy of the queue as a list.

        Parameters:
        - None.

        Returns:
        - A list containing all queue elements in order.
        """
        return self.items.copy()

    def clear(self):
        """
        Removes all elements from the queue.

        Parameters:
        - None.

        Returns:
        - None.
        """
        self.items = []
