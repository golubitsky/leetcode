from src.algorithms import miscellaneous as sut


def test_subsets_empty():
    input = []

    actual = sut.subsets(input)

    expected = [[]]
    assert actual == expected


def test_subsets_one_element():
    input = [1]

    actual = sut.subsets(input)

    expected = [[], [1]]
    assert actual == expected


def test_subsets_multiple_elements():
    # arrange
    input = [1, 2, 3]

    # act
    actual = sut.subsets(input)

    # convert to sets to disregard order of elements
    actual_sets = list(map(set, actual))

    # assert
    expected = [[], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]]
    for item in expected:
        assert set(item) in actual_sets

    # also ensure same number of elements
    assert len(actual) == len(expected)


def test_max_after_all_operations():
    operations = [
        [1, 2, 100],
        [2, 5, 100],
        [3, 4, 100]
    ]
    n = 5

    actual = sut.max_after_all_operations(n, operations)

    assert actual == 200
