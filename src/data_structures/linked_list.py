class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def peek_head(self):
        if(self.head):
            return self.head.data

        return None

    def peek_tail(self):
        if(self.tail):
            return self.tail.data

        return None

    def insert_at_head(self, data):
        if (self.tail is self.head is None):  # list empty
            self.tail = self.head = Node(data)
        elif(self.tail is self.head):  # one node
            self.head, self.head.next = Node(data), self.head
            self.tail.previous = self.head
        else:  # multiple nodes
            self.head, self.head.next = Node(data), self.head
            self.head.next.previous = self.head

    def insert_at_tail(self, data):
        if (self.tail is self.head is None):  # list empty
            self.tail = self.head = Node(data)
        elif(self.tail is self.head):  # one node
            self.tail, self.tail.previous = Node(data), self.tail
            self.head.next = self.tail
        elif(self.tail):  # multiple nodes
            self.tail, self.tail.previous = Node(data), self.tail
            self.tail.previous.next = self.tail

    def _remove_for_one_or_zero_nodes(self):
        if(self.head is None):
            return None

        removed = self.head.data
        self.head = self.tail = None
        return removed

    def remove_at_head(self):
        if(self.head is self.tail):  # removing single element
            return self._remove_for_one_or_zero_nodes()

        if (self.head):
            removed, self.head = self.head.data, self.head.next
            return removed

        return None

    def remove_at_tail(self):
        if(self.head is self.tail):  # removing single element
            return self._remove_for_one_or_zero_nodes()

        if (self.tail):
            removed, self.tail = self.tail.data, self.tail.previous
            return removed

        return None

    def to_array_from_head(self):
        """
        Returns all data in an array, starting at head.

        This is obviously not performant because it uses a dynamic array.
        The point is to traverse correctly.
        """
        traversed = []

        current = self.head
        while(current):
            traversed.append(current.data)
            current = current.next

        return traversed

    def to_array_from_tail(self):
        """
        Returns all data in an array, starting at tail.
        """
        traversed = []

        current = self.tail
        while(current):
            traversed.append(current.data)
            current = current.previous

        return traversed


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
