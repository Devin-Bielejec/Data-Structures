# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Value is {self.value if self.value is not None else 'None'}, leftVal = {self.left.value if self.left is not None else 'None'}, and rightVal = {self.right.value if self.right is not None else 'None'}"

    # Insert the given value into the tree
    def insert(self, value):
        curNode = self

        def helper(node, value):
            # create a new BinarySearchTree
            if value > node.value:
                if node.right is None:
                    node.right = BinarySearchTree(value)
                else:
                    helper(node.right, value)
            elif value < node.value:
                if node.left is None:
                    node.left = BinarySearchTree(value)
                else:
                    helper(node.left, value)
            else:
                print("Cannot add value; it is a duplicate")

        helper(curNode, value)
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        curTree = self
        while curTree is not None:
            if target == curTree.value:
                return True
            elif target > curTree.value:
                curTree = curTree.right
            else:
                curTree = curTree.left
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        curTree = self
        maxVal = curTree.value
        while curTree.right:
            curTree = curTree.right
            maxVal = curTree.value
        return maxVal

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        def helper(node):
            if node.value is not None:
                cb(node.value)
            if node.left is not None:
                helper(node.left)
            if node.right is not None:
                helper(node.right)

        helper(self)
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
