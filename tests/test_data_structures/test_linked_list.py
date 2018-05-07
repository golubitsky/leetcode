from src.data_structures import linked_list
import unittest
import pytest


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.sut = linked_list.DoublyLinkedList()

    def test_is_empty_on_initialize(self):
        assert self.sut.is_empty() == True

    def test_is_not_empty_after_insert_at_head(self):
        self.sut.insert_at_head(2)
        assert self.sut.is_empty() == False

    def test_head_contains_item_inserted_at_head(self):
        self.sut.insert_at_head(1)
        assert self.sut.peek_head() == 1

    def test_head_contains_last_item_inserted_at_head(self):
        self.sut.insert_at_head(2)
        self.sut.insert_at_head(1)
        assert self.sut.peek_head() == 1

    def test_list_empty_after_insert_and_remove_at_head(self):
        self.sut.insert_at_head(1)
        self.sut.remove_at_head()
        assert self.sut.is_empty() == True

    def test_remove_at_head_returns_data_in_head(self):
        self.sut.insert_at_head(1)
        actual = self.sut.remove_at_head()
        assert actual == 1

    def test_head_contains_correct_item_after_remove(self):
        self.sut.insert_at_head(2)
        self.sut.insert_at_head(1)
        self.sut.remove_at_head()
        assert self.sut.peek_head() == 2

    def test_remove_at_head_returns_none_for_empty_list(self):
        assert self.sut.remove_at_head() == None

    def test_is_not_empty_after_insert_at_tail(self):
        self.sut.insert_at_tail(2)
        assert self.sut.is_empty() == False

    def test_tail_contains_item_inserted_at_tail(self):
        self.sut.insert_at_tail(1)
        assert self.sut.peek_tail() == 1

    def test_tail_contains_last_item_inserted_at_tail(self):
        self.sut.insert_at_tail(2)
        self.sut.insert_at_tail(1)
        assert self.sut.peek_tail() == 1

    def test_list_empty_after_insert_and_remove_at_tail(self):
        self.sut.insert_at_tail(1)
        self.sut.remove_at_tail()
        assert self.sut.is_empty() == True

    def test_remove_at_tail_returns_data_in_tail(self):
        self.sut.insert_at_tail(1)
        actual = self.sut.remove_at_tail()
        assert actual == 1

    def test_tail_contains_correct_item_after_remove(self):
        self.sut.insert_at_tail(2)
        self.sut.insert_at_tail(1)
        self.sut.remove_at_tail()
        assert self.sut.peek_tail() == 2

    def test_remove_at_tail_returns_none_for_empty_list(self):
        assert self.sut.remove_at_tail() == None

    def test_remove_at_tail_returns_none_correctly(self):
        self.sut.insert_at_tail(1)
        self.sut.remove_at_tail()
        assert self.sut.peek_tail() == None

    def test_head_pointer_correct_after_insert_at_tail(self):
        self.sut.insert_at_tail(1)
        assert self.sut.peek_head() == 1

    def test_tail_pointer_correct_after_insert_at_head(self):
        self.sut.insert_at_head(1)
        assert self.sut.peek_tail() == 1

    def test_tail_pointer_correct_after_remove_at_head(self):
        self.sut.insert_at_head(1)
        self.sut.remove_at_head()
        assert self.sut.peek_tail() == None

    def test_head_pointer_correct_after_remove_at_tail(self):
        self.sut.insert_at_head(1)
        self.sut.remove_at_tail()
        assert self.sut.peek_head() == None


test_data = [
    ([1, 2, 3]),
    ([7, 8, 9, 21, 33]),
]


@pytest.mark.parametrize("input", test_data)
def test_to_array_traversal(input):
    # arrange
    sut = linked_list.DoublyLinkedList()
    for data in input:
        sut.insert_at_tail(data)
    # act
    actual = sut.to_array_from_head()

    # assert
    assert actual == input


@pytest.mark.parametrize("input", test_data)
def test_to_array_reverse_traversal(input):
    # arrange
    sut = linked_list.DoublyLinkedList()
    for data in input:
        sut.insert_at_tail(data)
    # act
    actual = sut.to_array_from_tail()

    # assert
    assert actual == list(reversed(input))


def test_to_array_reverse_traversal_inserting_from_both_directions():
    # arrange
    sut = linked_list.DoublyLinkedList()
    sut.insert_at_tail(1)
    sut.insert_at_tail(2)
    sut.insert_at_head(0)
    # act
    actual = sut.to_array_from_tail()

    # assert
    assert actual == [2, 1, 0]
