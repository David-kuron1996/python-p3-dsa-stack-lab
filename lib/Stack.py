class Stack:
    def __init__(self, items=None, capacity=None):
        # Initialize the stack with a list of items
        if items is None:
            self.items = []
        else:
            self.items = list(items)
        # Set the maximum capacity of the stack
        self.capacity = capacity

    def push(self, item):
        # Add an item to the top of the stack
        # FIX: Only push if the stack is not full
        if self.capacity is None or not self.full():
            self.items.append(item)

    def pop(self):
        # Remove and return the item from the top of the stack
        # FIX: Return None if the stack is empty
        if self.isEmpty():
            return None
        return self.items.pop()

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def isEmpty(self):
        # Return True if the stack is empty, False otherwise
        return len(self.items) == 0

    def full(self):
        # Return True if the stack is at full capacity, False otherwise
        if self.capacity is None:
            return False
        return len(self.items) >= self.capacity

    def search(self, item):
        # Return the distance of the item from the top of the stack
        try:
            # index() finds the first occurrence from the bottom
            # We calculate the distance from the top
            return len(self.items) - self.items.index(item) - 1
        except ValueError:
            # Return -1 if the item is not in the stack
            return -1