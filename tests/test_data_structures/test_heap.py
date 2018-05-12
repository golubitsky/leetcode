from src.data_structures import heap
import unittest


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.sut = heap.MinHeap()

    def test_size_on_init(self):
        assert self.sut.size() == 0

    def test_size_on_insert(self):
        self.sut.insert(1)
        self.sut.insert(1)

        assert self.sut.size() == 2

    def test_extract_min(self):
        # arrange
        self.sut.insert(2)
        self.sut.insert(3)
        self.sut.insert(8)
        expected_min = -2
        self.sut.insert(expected_min)

        # act
        actual = self.sut.extract_min()

        # assert
        assert actual == expected_min

    def test_extract_min_many_times(self):
        self.sut.insert(2)
        self.sut.insert(3)
        self.sut.insert(8)
        self.sut.extract_min()
        self.sut.extract_min()

        assert self.sut.extract_min() == 8
