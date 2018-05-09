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
from collections import defaultdict
import math


def dfs(parent_of, node, all_paths, current_path):
    current_path.insert_at_tail(node)

    # path ends here
    if (node not in parent_of):
        reversed_path = current_path.to_array_from_tail()
        all_paths.insert_at_tail(reversed_path)
    else:
        for parent in parent_of[node]:
            dfs(parent_of, parent, all_paths, current_path)

    # backtrack
    current_path.remove_at_tail()


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

    # to trace our path back when we find the target
    parent_of = defaultdict(lambda: [])
    depth = defaultdict(lambda: math.inf)
    depth[beginWord] = 0
    queue = Queue()
    queue.enqueue(beginWord)

    success = False
    while(not queue.is_empty()):
        current = queue.dequeue()
        if (current == endWord):
            success = True

        for child in graph.get_neighbors(current):
            not_encountered_yet = depth[child] == math.inf
            already_encountered_at_same_depth = depth[child] == depth[current] + 1

            if (not_encountered_yet):
                depth[child] = depth[current] + 1
                parent_of[child].append(current)
                queue.enqueue(child)
            elif(already_encountered_at_same_depth):
                parent_of[child].append(current)

    if success:
        all_paths = DoublyLinkedList()
        current_path = DoublyLinkedList()
        dfs(parent_of, endWord, all_paths, current_path)
        return all_paths.to_array_from_head()
    else:
        return []
