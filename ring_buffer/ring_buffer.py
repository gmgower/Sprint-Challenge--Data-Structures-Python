  
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_node = None # a, b, c, d
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check size of the storage is less than the capacity
        if len(self.storage) < self.capacity:
            # add to tail previous
            self.storage.add_to_tail(item)
            # set current node variable to the head 
            self.current_node = self.storage.head
        # check if the capacity as been reached


    def get(self):
        pass