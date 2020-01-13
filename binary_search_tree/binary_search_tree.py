import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #create a new BinarySearchTree
        if value > self.value:
            self.right = BinarySearchTree(value)
        elif value < self.value:
            self.left = BinarySearchTree(value)
        else:
            print("Cannot add value; it is a duplicate");
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        curTree = self
        while curTree.value:
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

   
