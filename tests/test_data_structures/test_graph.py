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