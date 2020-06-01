class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # referenc to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference to head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        
        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        # H5, N -> 4, N -> 3, N -> 2, N -> 1, N -> None      
        # declare values
        current = self.head

        #while there is a current node in the list
        while current:
            # stores current.get_next value in a temp var next_node 
            next_node = current.get_next()
            # points to the previous node
            current.set_next(prev)
            # update prev to the current
            prev = current
            # sets current variable into the next_node
            current = next_node
        # resets the list to point to a new head
        self.head = prev

# Test cases 
# list = LinkedList()
# list.add_to_head(1)
# list.add_to_head(2)
# list.add_to_head(3)
# list.add_to_head(4)
# list.add_to_head(5)
# print(list.head.value) # should be 5
# print(list.head.get_next().value) # should be 4
# list.reverse_list(list.head, None)
# print(list.head.value) # should be 1
# print(list.head.get_next().value) # should be 2
