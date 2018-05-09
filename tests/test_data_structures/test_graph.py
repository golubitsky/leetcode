from src.data_structures import graph
import unittest
import pytest


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sut = graph.Graph()

    def test_add_node(self):
        # arrange
        self.sut.add_node('test')

        # act / assert
        assert self.sut.node_exists('test')

    def test_add_edge(self):
        # arrange
        self.sut.add_edge('a', 'b')

        # act / assert
        assert self.sut.edge_exists('a', 'b')

    def test_get_neighbors(self):
        # arrange
        self.sut.add_edge('a', 'b')
        self.sut.add_edge('a', 'c')

        # act
        actual = self.sut.get_neighbors('a')

        # assert
        assert actual == ['b', 'c']

    def test_remove_node(self):
        # arrange
        self.sut.add_node('test')

        # act
        self.sut.remove_node('test')

        # assert
        assert not self.sut.node_exists('test')
    
    def test_remove_node_removes_edge_from_neighbor(self):
        # arrange
        self.sut.add_edge('a', 'b')

        # act
        self.sut.remove_node('a')

        # assert
        assert not self.sut.edge_exists('b', 'a')

    def test_remove_edge_undirected(self):
        # arrange
        self.sut.add_edge('a', 'b')

        # act
        self.sut.remove_edge('a', 'b')

        # assert
        assert not self.sut.edge_exists('a', 'b')
        assert not self.sut.edge_exists('b', 'a')

    def test_remove_edge_leaves_nodes(self):
        # arrange
        self.sut.add_edge('a', 'b')

        # act
        self.sut.remove_edge('a', 'b')

        # assert
        assert self.sut.node_exists('a')
        assert self.sut.node_exists('b')

    def test_from_list_throws_for_not_same_length_words(self):
        # arrange
        words = ["ab", "abc"]

        # act / assert
        self.assertRaises(
            ValueError, graph.Graph.from_same_length_word_list, words)

    def test_from_list_inserts_all_words(self):
        # arrange
        words = ["ab", "ac", "bc"]

        # act
        actual = graph.Graph.from_same_length_word_list(words)

        # assert
        for word in words:
            assert actual.node_exists(word)

    def test_from_list_creates_appropriate_edges(self):
        # arrange
        words = ["ab", "ac", "bc"]

        # act
        actual = graph.Graph.from_same_length_word_list(words)

        # assert
        assert actual.edge_exists("ab", "ac")
        assert actual.edge_exists("ac", "ab")
        assert actual.edge_exists("bc", "ac")
        assert actual.edge_exists("ac", "bc")