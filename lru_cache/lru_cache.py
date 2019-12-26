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


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        #dll key entriers in correct order
        self.dll = DoublyLinkedList()
        #dict fast acces to every node by key to find value
        self.hash = {}
        #max number of nodes it can hold
        self.limit = limit
        #current number of nodes it is holding
        self.length = self.dll.__len__()        
        pass

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #get value of key

        #move key value pair to end of order

        #return value of key or None

        if self.hash[key]:
            #Get node from dll
            self.dll.move_to_end(self.dll.)
            return self.hash[key]
        else:
            return None
        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #If the key already exists
        if self.hash[key]:
            #Overwrite value in hash
            self.hash[key] = value
            #move to front
            self.dll.move_to_front(self.hash[key]) 
        else:
            #If we add 1, will we be over the limit
            if self.dll.length + 1 > self.limit:
                #Remove oldest entry
                self.dll.remove_from_tail()
            
            #Add key to head
            self.dll.add_to_head(key)
            #Add to hash
            self.hash[key] = self.dll.head
            pass
