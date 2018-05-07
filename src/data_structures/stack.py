class Stack:
    def __init__(self):
        self.store = []

    def _is_empty(self):
        return len(self.store) == 0

    def push(self, item):
        self.store.append(item)

    def pop(self):
        if(self._is_empty()):
            return None

        return self.store.pop()

    def peek(self):
        if(self._is_empty()):
            return None

        return self.store[-1]
