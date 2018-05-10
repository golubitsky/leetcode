class BinaryTreeNode:

    @classmethod
    def __construct_from_list(self, list):
        raise NotImplementedError

    @classmethod
    def construct_from_list(self, list):
        """
        [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
        """
        raise NotImplementedError

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def _traverse_default_wrapper(self, traverse_fn):
        # append to this array as we traverse the tree
        arr = []

        def default_traverse_step(*args):
            return arr.append(args[0])

        # now call the appropriate traverse function
        traverse_fn(default_traverse_step, arr)

        return arr

    def traverse_in_order(self, traverse_step_func=None, *args):
        """
            While traversing in order, execute the provided function,
            passing in each node's data as well as an arbitrary number
            of provided arguments.

            If no traverse_step_func is provided, an array of the traversal
            will be returned.
        """
        if traverse_step_func is None:
            return self._traverse_default_wrapper(self.traverse_in_order)

        self.left and self.left.traverse_in_order(traverse_step_func, *args)
        traverse_step_func(self.data, *args)
        self.right and self.right.traverse_in_order(traverse_step_func, *args)

    def traverse_pre_order(self, traverse_step_func=None, *args):
        if traverse_step_func is None:
            return self._traverse_default_wrapper(self.traverse_pre_order)

        traverse_step_func(self.data, *args)
        self.left and self.left.traverse_pre_order(traverse_step_func, *args)
        self.right and self.right.traverse_pre_order(traverse_step_func, *args)

    def traverse_post_order(self, traverse_step_func=None, *args):
        if traverse_step_func is None:
            return self._traverse_default_wrapper(self.traverse_post_order)

        self.left and self.left.traverse_post_order(traverse_step_func, *args)
        self.right and self.right.traverse_post_order(
            traverse_step_func, *args)
        traverse_step_func(self.data, *args)
