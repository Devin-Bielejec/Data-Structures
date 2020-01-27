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
        # New Next is current value, so previous is current, and next is current next
        self.next = ListNode(value, self, current_next)
        # If next exists, current Next's prev needs to links to value we're inserting
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
        # If Previous, previous's next now points to this' next, skipping current
        if self.prev:
            self.prev.next = self.next
        # If Next, next's previous now points to this previous, skipping current
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
# 4 Cases
# Case 1: None
# Case 2: head/tail
# Case 3: head, tail
# Case 4: head, item, tail


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
        if self.head:
            currentHead = self.head
            # insert value before current head, so currentHead is connected to new head
            currentHead.insert_before(value)
            # make head equal to head's previous value
            self.head = currentHead.prev

            # if head/tail, tail prev points to new self.head
            if currentHead == self.tail:
                self.tail = currentHead
                self.tail.prev = self.head
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length = self.length + 1
        pass

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        currentHead = self.head
        if currentHead is None:
            return None

        # Reassigning new head
        if currentHead.next is not None:
            self.head = currentHead.next
            # If new head next is None, head is tail
            if self.head.next is None:
                self.tail = self.head
        else:
            self.head = None
            self.tail = None
        self.length = self.length - 1

        return currentHead.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # insert after tail
        if self.tail:
            currentTail = self.tail
            currentTail.insert_after(value)
            self.tail = currentTail.next
            if currentTail == self.head:
                self.head = currentTail
        else:
            self.tail = ListNode(value)
            self.head = self.tail
        self.length = self.length + 1
        pass

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # Case 1: {tail/head}
        # Case 2: {head, tail}
        # Case 3: {head, item, tail}
        if self.tail:
            currentTail = self.tail
            currentTail.delete()
            self.length = self.length - 1

            if currentTail == self.head:
                self.head = None
                self.tail = None
            else:
                self.tail = currentTail.prev

            return currentTail.value
        else:
            return None
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        #{head/tail}, {head, tail}, {head, item, tail}
        # Add node to front of list
        self.add_to_head(node.value)
        # Delete node
        node.delete()
        # Add to head increases length but delete doesn't decrease
        self.length = self.length - 1
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        #head, item, tail

        # add to tail
        self.add_to_tail(node.value)
        if node == self.head:
            self.head = self.head.next
        # delete
        node.delete()
        # Add to tail increases length but delete doesn't decrease
        self.length = self.length - 1
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
        pass

    """Returns the highest value currently in the list"""

    def get_max(self):
        max = self.head.value
        current = self.head
        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next
        return max
