import unittest
from src import hello_world


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.func = hello_world.add
        pass

    def test_1(self):
        self.assertEqual(self.func(2, 2), 4), "More info about the failure!"

    def test_2(self):
        self.assertEqual(self.func(2, 3), 5)
