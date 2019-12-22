"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        #New Next is current value, so previous is current, and next is current next
        self.next = ListNode(value, self, current_next)
        #If next exists, current Next's prev needs to links to value we're inserting
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        #If Previous, previous's next now points to this' next, skipping current
        if self.prev:
            self.prev.next = self.next
        #If Next, next's previous now points to this previous, skipping current
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        print(value)
        #current Head, used later
        currentHead = self.head
        #Make current head listNode, linking to currentHead as next
        if self.head is not None:
            self.head = ListNode(value, self.head.prev, currentHead)
        else:
            self.head = ListNode(value)

        #Replace current Head's previoius with new current Head
        currentHead.prev = self.head
        #Added to length
        self.length = self.length + 1
        pass

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #remove head by making head's next equal to head
        currentHead = self.head
        if self.head is not None:
            self.head = self.head.next
        if self.head is None:
            self.tail = None
        #Removing, length changes
        self.length = self.length - 1
        return currentHead.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        added = ListNode(value, self.tail, None)
        self.tail.next = added
        self.length = self.length + 1
        pass

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        removed = self.tail
        if self.tail is not None:
            self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        self.length = self.length - 1
        return removed.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass

