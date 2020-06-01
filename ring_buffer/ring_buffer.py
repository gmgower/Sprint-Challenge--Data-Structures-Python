  
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None # a, b, c, d
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check size of the storage is less than the capacity
        if len(self.storage) < self.capacity:
            #add item to the tail
            self.storage.add_to_tail(item)
            return
        #if current has no value
        if self.current is None:
            self.current = self.storage.head
        #sets the current value to the item
        self.current.value = item
        #set current to the next  value
        self.current = self.current.next
       

    def get(self):
        # create a blank array 
        buffer = []
        # declare a current variable & set it to the head of the
        current = self.storage.head
        # while there still a current value
        while current:
            # append the value to the buffer
            buffer.append(current.value)
            # move the current reference to the next node in the
            current = current.next
        return buffer

"""
    ```python
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
```
"""