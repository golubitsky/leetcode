import pytest
import importlib
solution = importlib.import_module('src.020_valid_parentheses')


test_data = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("()", True),
    ("{[]}", True),
]


@pytest.mark.parametrize("input,expected", test_data)
def test_is_valid(input, expected):
    assert solution.is_valid(input) == expected

def test_is_valid_empty():
    assert solution.is_valid("") == True

@pytest.mark.parametrize("input", ["{", "{{}"])
def test_is_not_valid_odd_number(input):
    assert solution.is_valid(input) == False
