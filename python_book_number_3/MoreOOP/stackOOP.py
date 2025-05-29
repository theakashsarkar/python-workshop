class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        if len(self.items) < 5:
            self.items.append(item)
    
    def pop(self):
        return self.items.pop()
        