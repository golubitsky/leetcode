from src.data_structures import binary_tree


# Given a binary tree, find the length of the longest path where
# each node in the path has the same value.
# This path may or may not pass through the root.

# Note: The length of path between two nodes is represented
# by the number of edges between them.

# Example 1:

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:

# 2
# Example 2:

# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:

# 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

def longest_univalue_path(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    working_data = {
        'longest': 0,
        'current': -1,  # we will count edges, not nodes
        'previous': -0.00001  # value we expect not to see
    }

    def check_path(data, w):
        if data == w['previous']:
            w['current'] += 1
        else:
            w['current'] = 0

        if w['current'] > w['longest']:
            w['longest'] = w['current']

        w['previous'] = data

    root.traverse_in_order(check_path, working_data)

    return working_data['longest']
