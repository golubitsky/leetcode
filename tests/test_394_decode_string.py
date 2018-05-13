import importlib
solution = importlib.import_module('src.394_decode_string')
import pytest

test_data = [
    ("4[2[ab]]", 1, 7),
    ("4[2[ab]]", 3, 6),
    ("3[a2[c]]", 1, 7),
    ("2[abc]3[cd]ef", 1, 5),
]


@pytest.mark.parametrize("input,start, match", test_data)
def test_find_matching_paren(input, start, match):
    assert solution.find_matching_bracket(input, start) == match

test_data = [
    ("3[a]", "aaa"),
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ("2[zz3[a]bc]", "zzaaabczzaaabc"),
]


@pytest.mark.parametrize("input,expected", test_data)
def test_decode_string(input, expected):
    assert solution.decode_string(input) == expected
