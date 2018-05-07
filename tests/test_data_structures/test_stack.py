from src.data_structures import stack
import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.sut = stack.Stack()

    def test_is_empty_on_initialize(self):
        assert self.sut.peek() == None

    def test_peek_shows_last_pushed_item(self):
        self.sut.push(1)
        assert self.sut.peek() == 1

    def test_pop_top_item(self):
        # arrange
        self.sut.push(1)
        self.sut.push(2)

        # act / assert
        assert self.sut.pop() == 2

    def test_ensure_pop_removes_item(self):
        # arrange
        self.sut.push(1)
        self.sut.push(2)

        # act
        self.sut.pop()

        # assert
        assert self.sut.peek() == 1

    def test_pop_empty_returns_none(self):
        assert self.sut.pop() == None