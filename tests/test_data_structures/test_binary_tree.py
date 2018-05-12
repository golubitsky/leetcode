from src.data_structures.binary_tree import BinaryTreeNode

# arrange
#   1
#  2 3
# 4   5
sut = BinaryTreeNode(1)
sut.left = BinaryTreeNode(2)
sut.left.left = BinaryTreeNode(4)
sut.right = BinaryTreeNode(3)
sut.right.right = BinaryTreeNode(5)


def test_traverse_in_order():
    assert sut.traverse_in_order() == [4, 2, 1, 3, 5]


def test_traverse_pre_order():
    assert sut.traverse_pre_order() == [1, 2, 4, 3, 5]


def test_traverse_post_order():
    assert sut.traverse_post_order() == [4, 2, 5, 3, 1]


def test_traverse_level_order():
    assert sut.traverse_level_order() == [1, 2, 3, 4, 5]


def _setup_traverse_func_test():
    d = {
        'total': 0
    }

    def func(data, *args): d['total'] += data + args[0]

    return d, func


def test_traverse_in_order_accepts_func_and_args():
    # arrange
    external_data, func = _setup_traverse_func_test()

    # act
    sut.traverse_in_order(func, 1)

    # assert
    assert external_data['total'] == 20


def test_traverse_pre_order_accepts_func_and_args():
    # arrange
    external_data, func = _setup_traverse_func_test()

    # act
    sut.traverse_pre_order(func, 1)

    # assert
    assert external_data['total'] == 20


def test_traverse_post_order_accepts_func_and_args():
    # arrange
    external_data, func = _setup_traverse_func_test()

    # act
    sut.traverse_pre_order(func, 1)

    # assert
    assert external_data['total'] == 20


def test_construct_from_list():
    # arrange
    # e.g.
    #    4
    #  7   3
    #     1
    input = [4, 7, 3, None, None, 1]

    sut = BinaryTreeNode.construct_from_list(input)

    # act / assert
    assert sut.traverse_level_order() == [4, 7, 3, 1]


def test_construct_from_list_complex():
    # arrange
    input = [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6,
             None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2]

    # act
    sut = BinaryTreeNode.construct_from_list(input)
    actual = sut.traverse_level_order()

    # assert
    expected = list(filter(lambda x: x is not None, input))
    assert actual == expected
