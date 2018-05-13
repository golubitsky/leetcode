import importlib
import pytest
solution = importlib.import_module('src.724_find_pivot_index')


def test_empty_no_solution():
    assert solution.pivot_index([]) == -1


def test_returns_neg_1_for_no_solution():
    input = [1, 2, 3]
    assert solution.pivot_index(input) == -1


test_data = [
    ([1, 7, 3, 6, 5, 6], 3),
    ([-1, -1, -1, 0, 1, 1], 0),
    ([-1, -1, 0, 1, 1, 0], 5),
]


@pytest.mark.parametrize("input,expected", test_data)
def test_returns_index_if_solution_exists(input, expected):
    assert solution.pivot_index(input) == expected
