import pytest
import importlib
solution = importlib.import_module('src.007_reverse_integer')

test_data = [
    (123, 321),
    (-123, -321),
    (120, 21)
]


@pytest.mark.parametrize("input,expected", test_data)
def test_reverse(input, expected):
    assert solution.reverse(input) == expected
