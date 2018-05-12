from src.data_structures.queue import Queue


class BinaryTreeNode:

    __unassigned = -1

    @classmethod
    def __node_for_construction(self, data):
        if(data is None):
            return data

        node = BinaryTreeNode(data)
        node.left = self.__unassigned
        node.right = self.__unassigned

        return node

    @classmethod
    def construct_from_list(self, list):
        """
            Creates a binary tree from a level-ordered list of values.
            Empty children for existing nodes should be specified with
            None.

            e.g. [4,7,3,None,None,1] yields a tree of shape:
                 4
                / \
               7   3
                  /
                 1
        """
        queue = Queue()
        root = self.__node_for_construction(list[0])
        current = root

        for data in list[1:]:
            new = self.__node_for_construction(data)
            if new is not None:
                queue.enqueue(new)

            if(current.left == self.__unassigned):
                current.left = new
            elif(current.right == self.__unassigned):
                current.right = new
            else:  # current node is full
                current = queue.dequeue()
                current.left = new

        # clean up (ensure unassigned values are represented as None)
        queue = Queue()
        queue.enqueue(root)
        while(not queue.is_empty()):
            current = queue.dequeue()
            if(current.left == self.__unassigned):
                current.left = None
            elif(current.left):
                queue.enqueue(current.left)

            if(current.right == self.__unassigned):
                current.right = None
            elif(current.right):
                queue.enqueue(current.right)

        return root

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

    def traverse_level_order(self):
        queue = Queue()
        queue.enqueue(self)

        arr = []

        while(not queue.is_empty()):
            current = queue.dequeue()
            arr.append(current.data)
            for child in [current.left, current.right]:
                if(child):
                    queue.enqueue(child)

        return arr
