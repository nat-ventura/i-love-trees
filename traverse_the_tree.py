import numpy.random as nprnd
from binarytree import Node, show

class BSTNode(Node):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.parent = None
        self.right = None

    def left_rotate(self):
        if self.right == None: return
        new_parent = self.right
        new_parent.parent = self.parent
        new_right = new_parent.left
        new_parent.left = self
        self.right = new_right

        if self.is_right_node():
            self.parent.right = new_parent

        if self.is_left_node():
            self.parent.left = new_parent

        self.parent = new_parent

        return new_parent

    def right_rotate(self):
        if self.left == None: return
        new_parent = self.left
        new_parent.parent = self.parent
        new_left = new_parent.right
        new_parent.right = self
        self.left = new_left

        if self.is_right_node():
            self.parent.right = new_parent

        if self.is_left_node():
            self.parent.left = new_parent

        self.parent = new_parent

        return new_parent

    def is_right_node(self):
        if self.parent == None: return False
        if self.parent.right == self: return True

    def is_left_node(self):
        if self.parent == None: return False
        if self.parent.left == self: return True

    def add(self, new_node):
        if new_node.value < self.value:
            if self.left == None:
                self.left = new_node
                new_node.parent = self
            else:
                self.left.add(new_node)
        else:
            if self.right == None:
                self.right = new_node
                new_node.parent = self
            else:
                self.right.add(new_node)

    def find(self, valueToLookFor):
        if self.value == valueToLookFor:
            return self

        if valueToLookFor >= self.value:
            if self.right == None: return None
            return self.right.find(valueToLookFor)

        if valueToLookFor < self.value:
            if self.left == None: return None
            return self.left.find(valueToLookFor)

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = BSTNode(value)

        if self.root is not None:
            self.root.add(new_node)
        else:
            self.root = new_node

    def left_rotate(self, node):
        new_parent = node.left_rotate()
        if node == self.root:
            self.root = new_parent

    def right_rotate(self, node):
        new_parent = node.right_rotate()
        if node == self.root:
            self.root = new_parent

    def find(self, value):
        if self.root == None: return None
        if self.root.value == value: return self.root
        return self.root.find(value)

def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = BST()
numbers = random_numbers(10)
value_to_rotate = numbers[len(numbers) / 2]

for i in numbers:
    tree.add(i)

show(tree.root)

print ("Attempting to rotate " + str(value_to_rotate) + ".")
node_to_rotate = tree.find(value_to_rotate)
tree.left_rotate(node_to_rotate)
show(tree.root)

# tree = BST()
# tree.add(1)
# tree.add(2)
# print(tree.root.value)