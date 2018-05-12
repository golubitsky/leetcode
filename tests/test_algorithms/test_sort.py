from src.algorithms import sort as sut
import pytest


def test_merge():
    assert(sut._merge([2],[1,3])) == [1,2,3]

test_data = [
    ([3,1,2], [1,2,3]),
    ([5,7,9,2,4,3], [2,3,4,5,7,9]),
]

@pytest.mark.parametrize("input,sorted", test_data)
def test_merge_sort(input, sorted):
    assert sut.merge_sort(input) == sorted

@pytest.mark.parametrize("input,sorted", test_data)
def test_quick_sort(input, sorted):
    assert sut.quick_sort(input) == sorted
