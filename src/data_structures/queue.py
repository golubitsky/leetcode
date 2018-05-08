from src.data_structures import linked_list


class Queue:
    def __init__(self):
        self.list = linked_list.DoublyLinkedList()

    def is_empty(self):
        return self.list.peek_head() is None

    def enqueue(self, data):
        self.list.insert_at_tail(data)

    def dequeue(self):
        return self.list.remove_at_head()