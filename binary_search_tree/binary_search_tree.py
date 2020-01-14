import sys
sys.path.append('../queue_and_stack/')
from dll_stack import Stack
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
        def helper(node):
            if node:
                helper(node.left)
                print(node.value)
                helper(node.right)
        helper(node)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        cue = Queue()
        cue.enqueue(node)
        while cue.len() > 0:
            firstNode = cue.dequeue()
            print(firstNode.value)
            # if left or right enqueue
            if firstNode.left is not None:
                cue.enqueue(firstNode.left)
            if firstNode.right is not None:
                cue.enqueue(firstNode.right)
            
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

