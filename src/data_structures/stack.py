from src.data_structures.linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.store = DoublyLinkedList()

    def is_empty(self):
        return self.store.peek_head() == None

    def push(self, item):
        self.store.insert_at_head(item)

    def pop(self):
        if(self.is_empty()):
            return None

        return self.store.remove_at_head()

    def peek(self):
        return self.store.peek_head()
