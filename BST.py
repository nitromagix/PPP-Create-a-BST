

# Part 1: Create a BSTNode class

from curses import flash
from tkinter.messagebox import NO
from xml.dom.pulldom import START_DOCUMENT


class BSTNode:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.data}"

    def __repr__(self) -> str:
        return f"{self.data}"

    @staticmethod
    def new_node_from(input):
        if type(input) is int:
            return BSTNode(input)
        elif type(input) is BSTNode:
            return BSTNode(input.data, input.left, input.right)
        else:
            raise ValueError("The input should be of type int or type BSTNode")


# Part 2: Create a BST class
# Part 3: Add functionality to your BST class

class BST:
    contents = []

    def __init__(self, root=None) -> None:
        if not root is None:
            self.root = BSTNode.new_node_from(root)
        else:
          self.root = None

    def __str__(self) -> str:
        if self.root is None:
            return "The tree is empty"

        self.output = "\n"

        self.print_tree(self.root)
        return self.output

    def __repr__(self) -> str:
        pass

    def print_tree(self, node, level=0) -> None:
        if node != None:
            self.print_tree(node.right, level + 1)
            self.output += " " * 4 * level + " -> " + str(node) + "\n"
            self.print_tree(node.left, level + 1)

    def add(self, input) -> None:
        # input is already in the list
        if self.contains(input):
            return
        
        # create new node from input  
        new_node = BSTNode.new_node_from(input)
        
        # list is empty - new node becomes root
        if self.is_empty():
            self.root = new_node
            self.contents.append(new_node.data)
            return
        
        # add_node helper function
        def add_node(node, node_to_add):
            if node_to_add.data < node.data:
                if node.left is None:
                    node.left = node_to_add
                    self.contents.append(node_to_add.data)
                else:
                    add_node(node.left, node_to_add)
            elif node_to_add.data > node.data:
                if node.right is None:
                    node.right = node_to_add
                    self.contents.append(node_to_add.data)
                else:
                    add_node(node.right, node_to_add)
        
        # add the node
        add_node(self.root, new_node)

    def contains(self, input):
        return input in self.contents
      
    def is_empty(self):
        return self.root is None



# node1 = BSTNode(3)
# print(node1)  # 3
# node2 = BSTNode(4, left=node1)
# print(node2)  # 4
# node3 = BSTNode()
# print(node3)  # None
# node3.data = 5
# print(node3)  # 5
# bst = BST()
# print(bst)
# bst.root = node2
# node2.right = node3
# print(bst)

#create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)
print(bst)
print(bst.contents)