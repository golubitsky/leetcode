from src.data_structures import queue
import unittest


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.sut = queue.Queue()

    def test_empty_by_default(self):
        assert self.sut.is_empty() == True

    def test_not_empty_if_element_enqueued(self):
        self.sut.enqueue(1)

        assert self.sut.is_empty() == False

    def test_dequeues_first_in_element(self):
        first = 7
        self.sut.enqueue(first)
        self.sut.enqueue(1)
        self.sut.enqueue(1)
        self.sut.enqueue(1)

        assert self.sut.dequeue() == first
        
    def test_dequeues_correct_element(self):
        self.sut.enqueue(1)
        self.sut.enqueue(2)
        self.sut.dequeue()        
        self.sut.enqueue(3)
        actual = self.sut.dequeue()
        
        assert actual == 2
