import pytest
import importlib
solution = importlib.import_module('src.007_reverse_integer')

test_data = [
    (123, 321),
    (-123, -321),
    (120, 21)
]


@pytest.mark.parametrize("input,expected", test_data)
def test_reverse_works(input, expected):
    assert solution.reverse(input) == expected


@pytest.mark.parametrize("input", [99999999999999, -9999999999999])
def test_should_return_zero_when_reversed_integer_overflows(input):
    print(input)
    assert solution.reverse(input) == 0
