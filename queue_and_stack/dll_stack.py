import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # we can add/remove from the back of the dll
        self.storage = DoublyLinkedList()

    def push(self, value):
        #add to back
        self.storage.add_to_tail(value)
        pass

    def pop(self):
        #return last item
        return self.storage.remove_from_tail()
        

    def len(self):
        return self.storage.__len__()