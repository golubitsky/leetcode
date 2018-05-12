class MinHeap():
    def __init__(self):
        self.store = []

    def _left_child(self, index):
        return index*2 + 1

    def _right_child(self, index):
        return index*2 + 2

    def _parent(self, index):
        if(index % 2 == 0):
            return index // 2 - 1
        else:
            return index // 2

    def _swap(self, i, j):
        self.store[i], self.store[j] = self.store[j], self.store[i]

    def _heapify(self):
        # TODO generalize for maxheap
        size = self.size()
        if(size <= 1):
            return

        cur_index = 0
        while True:
            left_child = self._left_child(cur_index)
            right_child = self._right_child(cur_index)
            if(left_child >= size and right_child >= size):
                break
            elif(left_child < size and right_child < size):
                if(self.store[cur_index] < self.store[left_child] and
                   self.store[cur_index] < self.store[right_child]):
                    # done!
                    break

                if(self.store[left_child] < self.store[right_child]):
                    if(self.store[left_child] < self.store[cur_index]):
                        self._swap(cur_index, left_child)
                        cur_index = left_child
                else:
                    if(self.store[right_child] < self.store[cur_index]):
                        self._swap(cur_index, right_child)
                        cur_index = right_child
            elif(left_child < size):
                # this is the last possible swap
                if(self.store[left_child] < self.store[cur_index]):
                    self._swap(cur_index, left_child)
                # done!
                break

    def insert(self, value):
        self.store.append(value)
        cur_index = len(self.store) - 1

        while cur_index != 0:
            parent_index = self._parent(cur_index)
            # TODO generalize for maxheap
            if self.store[parent_index] > self.store[cur_index]:
                self._swap(parent_index, cur_index)
                cur_index = parent_index
            else:
                break

    def extract_min(self):
        m, self.store = self.store[0], self.store[1:]
        self._heapify()
        return m

    def size(self):
        return len(self.store)
