import importlib
solution = importlib.import_module('src.687_longest_univalue_path')
from src.data_structures.binary_tree import BinaryTreeNode


def test_pass_through_args():
    def inner(*args):
        return args

    def outer(*args):
        return inner("0", *args, "c")

    assert outer("a", "b") == ("0", "a", "b", "c")


def test_univalue_path_1():
    #               5
    #              / \
    #             4   5
    #            / \   \
    #           1   1   5
    sut = BinaryTreeNode(5)
    sut.left = BinaryTreeNode(4)
    sut.right = BinaryTreeNode(5)
    sut.left.left = BinaryTreeNode(1)
    sut.left.right = BinaryTreeNode(1)
    sut.right.right = BinaryTreeNode(5)

    # act
    actual = solution.longest_univalue_path(sut)

    # assert
    assert actual == 2

def test_univalue_path_2():
    #               1
    #              / \
    #             4   5
    #            / \   \
    #           4   4   5
    sut = BinaryTreeNode(1)
    sut.left = BinaryTreeNode(4)
    sut.right = BinaryTreeNode(5)
    sut.left.left = BinaryTreeNode(4)
    sut.left.right = BinaryTreeNode(4)
    sut.right.right = BinaryTreeNode(5)

    # act
    actual = solution.longest_univalue_path(sut)

    # assert
    assert actual == 2
