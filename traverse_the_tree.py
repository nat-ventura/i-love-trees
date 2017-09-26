import numpy.random as nprnd
from binarytree import Node, show

class BSTNode(Node):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, value):
        new_node = BSTNode(value)

        if self.root is not None:
            self.root.add(new_node)
        else: self.root = new_node

def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = BST()
for i in random_numbers(10):
    tree.add(i)

show(tree.root)

tree.add(1)
tree.add(2)
print(tree.root.value)

# left is always before right in depth first traversal