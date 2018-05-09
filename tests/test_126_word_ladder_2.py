import importlib
solution = importlib.import_module('src.126_word_ladder_2')


def test_find_ladders_finds_all_shortest_paths():
    # arrange
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

    # act
    actual = solution.find_ladders(begin_word, end_word, word_list)

    # assert
    expected = [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]

    assert actual == expected


def test_find_ladders_returns_empty_array_when_no_paths_found():
    # arrange
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log"]

    # act
    actual = solution.find_ladders(begin_word, end_word, word_list)

    # assert
    assert actual == []
