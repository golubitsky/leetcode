# Given two words (beginWord and endWord), and a dictionary's word list,
# find all shortest transformation sequence(s) from beginWord to endWord,
# such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord
# is not a transformed word.
# Note:

# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

from src.data_structures.graph import Graph
from src.data_structures.queue import Queue
from src.data_structures.linked_list import DoublyLinkedList


def trace_path_back(begin_word, end_word, parent_of):
    print(parent_of)
    if (end_word in parent_of):
        path = DoublyLinkedList()
        cur_word = end_word
        while(True):
            path.insert_at_head(cur_word)
            if (cur_word == begin_word):
                break

            cur_word = parent_of[cur_word]

        return path.to_array_from_head()


def find_ladders(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    # ensure we add the beginWord to the graph
    graph_words = [beginWord] + wordList
    graph = Graph.from_same_length_word_list(graph_words)

    encountered = set() # set parent
    parent_of = {}  # to trace our path back when we find the target

    queue = Queue()
    queue.enqueue(beginWord)

    depth = 0
    while(not queue.is_empty()):
        current_word = queue.dequeue()
        encountered.add(current_word)

        for child in graph.get_neighbors(current_word):
            if (child not in encountered):
                parent_of[child] = current_word
                queue.enqueue(child)
                encountered.add(child)

            if (child == endWord):
                return trace_path_back(beginWord, endWord, parent_of)