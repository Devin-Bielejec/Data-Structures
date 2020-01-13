from doubly_linked_list import DoublyLinkedList


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

# Head is most recently used


class LRUCache:
    """
    max number of nodes it can hold
    the current number of nodes it is holding
    a doubly-linked list that holds the key-value entries in the correct
    storage dict that provides fast access
    """

    def __init__(self, limit=10):
        # dll key entries in correct order
        self.dll = DoublyLinkedList()
        # dict fast acces to every node by key to find value
        self.hash = {}
        # max number of nodes it can hold
        self.limit = limit
        # current number of nodes it is holding
        self.length = self.dll.__len__()
        pass

    """
    Return value associated with key (from hash)

    move key to head
    """

    def get(self, key):
        # Get value of key if exists
        if key in self.hash:
            # Move the NODE to the head, so that it's most recently used

            # find NODE
            curNode = self.dll.head

            while curNode.value:
                if curNode.value == key:
                    print(curNode.value)
                    self.dll.move_to_front(curNode)
                    #if tail, make prev new tail
                    if curNode.next == None:
                        self.dll.tail = curNode.prev
                    break
                else:
                    curNode = curNode.next
            print(self.dll.head.value, self.dll.head.next.value,
                  self.dll.head.next.next.value, self.dll.tail.value)
            return self.hash[key]
        else:
            # Key doesn't exist
            return None

    """
    Add key value to front of cache

    Doesn't exist AND not full
    -add KEY to head
    Doesn't exists AND full
    -remove tail
    -add KEY to head

    exists
    -bring KEY up to head
    """

    def set(self, key, value):
        # If the key already exists
        if key in self.hash:
            # Overwrite value in hash
            self.hash[key] = value
            # move NODE to front - dll holds keys
            # get node (value, next)
            curNode = self.dll.head
            print(curNode.value, curNode.next)
            while curNode.value:
                if curNode.value == key:
                    self.dll.move_to_front(curNode)
                    break
                curNode = curNode.next
        else:
            # If we add 1, will we be over the limit
            if self.dll.length + 1 > self.limit:
                # Remove oldest entry
                curKey = self.dll.remove_from_tail()
                # redclare hash to current hash with curKey filtered out
                self.hash = {k: v for k, v in self.hash.items() if k != curKey}

            # Add key to head
            self.dll.add_to_head(key)
            # Add to hash
            self.hash[key] = value
            pass
