import time

class BSTNode:
    def __init__(self, value):  # value = 5
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #value < self.value look left
        if value < self.value:
            #if something is there already
            if self.left:
                #recurse left
                self.left.insert(value)
            #if not
            else:
                #insert left
                self.left = BSTNode(value)
        #value < self.value look right
        if value >= self.value:
            #if something is there already
            if self.right:
                #recurse right
                self.right.insert(value)
            #if not
            else:
                #insert right
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

        else:
            if self.left is not None:  # we have a left child
                return self.left.contains(target)  # hand the target off teh left child
            else:
                return False


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
