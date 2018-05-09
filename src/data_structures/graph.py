from collections import defaultdict


class Graph:
    """
        Currently only an undirected graph 
        built with directedness in mind.
        TODO: build directedness.
    """

    @classmethod
    def from_same_length_word_list(self, word_list):
        """
            Factory method to construct a graph using 
        """
        g = Graph()
        word_length = len(word_list[0])
        buckets = defaultdict(lambda: [])

        for word in word_list:
            if len(word) != word_length:
                raise ValueError("All words must be same length.")

            for i in range(len(word)):
                bucket = f"{word[:i]}_{word[i + 1:]}"
                buckets[bucket].append(word)

        for bucket in buckets:
            adjacent_words = buckets[bucket]
            for i in range(len(adjacent_words)):
                word = adjacent_words[i]
                other_words = adjacent_words[:i] + adjacent_words[i + 1:]
                for other_word in other_words:
                    g.add_edge(word, other_word)

        return g

    def __init__(self):
        self._nodes = {}  # data => node
        self._edges_out = {}  # data => list(nodes)
        # used when removing nodes
        self._edges_in = {}  # data => list(nodes)

    def add_node(self, data):
        self._nodes[data] = Node(data)
        self._edges_in[data] = []
        self._edges_out[data] = []

    def remove_node(self, data):
        del self._nodes[data]
        for neighbor_data in self._edges_in[data]:
            self._edges_out[neighbor_data].remove(data)

        del self._edges_in[data]
        del self._edges_out[data]

    def node_exists(self, data):
        return data in self._nodes

    def get_neighbors(self, data):
        return self._edges_out[data]

    def add_edge(self, data1, data2):
        if (not self.node_exists(data1)):
            self.add_node(data1)
        if (not self.node_exists(data2)):
            self.add_node(data2)

        if (not self.edge_exists(data1, data2)):
            self._edges_out[data1].append(data2)
            self._edges_in[data1].append(data2)
        if (not self.edge_exists(data2, data1)):
            self._edges_out[data2].append(data1)
            self._edges_in[data2].append(data1)

    def remove_edge(self, data1, data2):
        if (self.edge_exists(data1, data2)):
            self._edges_in[data1].remove(data2)
            self._edges_out[data1].remove(data2)
        if (self.edge_exists(data2, data1)):
            self._edges_in[data2].remove(data1)
            self._edges_out[data2].remove(data1)

    def edge_exists(self, data1, data2):
        return data2 in self._edges_out[data1]


class Node:
    def __init__(self, data):
        self.data = data
