import numpy.random as nprnd
from binarytree import Node, show
import pdb     # you can use pdb.set_trace() and it's like a debugger

class RBNode(Node):
    RED = True
    BLACK = False

    def __init__(self, number):
        self.left = None
        self.right = None
        self.parent = None
        self.color = self.RED
        self.set_number(number)

    def add(self, new_node):
        if new_node.number < self.number:
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

    def height(self):
        leftSubTreeHeight = 0
        rightSubTreeHeight = 0

        if self.left is not None:
            leftSubTreeHeight = self.left.height()

        if self.right is not None:
            rightSubTreeHeight = self.right.height()

        if leftSubTreeHeight > rightSubTreeHeight:
            maxHeight = leftSubTreeHeight
        else:
            maxHeight = rightSubTreeHeight

        return maxHeight + 1

    def left_rotate(self):
        if self.right == None: return
        new_parent = self.right
        new_parent.parent = self.parent
        new_right = new_parent.left

        if new_right is not None:
            new_right.parent = self

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

        if new_left is not None:
            new_left.parent = self

        new_parent.right = self
        self.left = new_left

        if self.is_right_node():
            self.parent.right = new_parent

        if self.is_left_node():
            self.parent.left = new_parent

        self.parent = new_parent

        return new_parent

    def uncle(self):
        p = self.parent

        if p is None: return None

        g = self.parent.parent

        if g is None: return None

        if p.is_left_node(): u = g.right
        else: u = g.left
        return u

    def is_right_node(self):
        if self.parent == None: return False
        if self.parent.right == self: return True

    def is_left_node(self):
        if self.parent == None: return False
        if self.parent.left == self: return True

    def toggle_color(self):
        self.set_color(not self.color)
        self.fix_value()

    def set_number(self, number):
        self.number = number
        self.fix_value()

    def set_color(self, color):
        self.color = color
        self.fix_value()

    def fix_value(self):
        if self.color == self.RED:
            appendString = 'R'
        else:
            appendString = 'B'

        self.value = str(self.number) + appendString

    def is_right_node(self):
        if self.parent == None: return False
        if self.parent.right == self: return True

    def is_left_node(self):
        if self.parent == None: return False
        if self.parent.left == self: return True

class RedBlackTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = RBNode(value)

        if self.root == None:
            self.root = new_node
            self.fix_violations(new_node)
            return

        self.root.add(new_node)
        if new_node.parent.color == RBNode.RED:
            self.fix_violations(new_node)

    def right_rotate(self, node):
        new_root = node.right_rotate()
        if node == self.root:
            self.root = new_root

    def left_rotate(self, node):
        new_root = node.left_rotate()
        if node == self.root:
            self.root = new_root

def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = RedBlackTree()

for i in random_numbers(10):
    print("\n\n\n")
    print("Inserting " + str(i))
    tree.add(i)
    show(tree.root)

show(tree.root)