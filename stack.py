class Stack:
    def __init__(self):
        # Initialize an empty list to store the stack elements
        self.items = []

    def push(self, item):
        # Append the item to the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the last item from the stack
        # If the stack is empty, raise an error
        if not self.is_empty():
            return self.items.pop()
        raise ValueError("The stack is empty.")

    def peek(self):
        # Return the last item from the stack without removing it
        # If the stack is empty, raise an error
        if not self.is_empty():
            return self.items[-1]
        raise ValueError("The stack is empty.")

    def is_empty(self):
        # Return true if the stack is empty, false otherwise
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.items)
