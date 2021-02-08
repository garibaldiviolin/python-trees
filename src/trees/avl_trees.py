from .binary_search_trees import BinarySearchTree, BinarySearchTreeNode


class AVLTreeNode(BinarySearchTreeNode):
    def __init__(self, value):
        self.value = value
        self.height = 0

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"


class AVLTree(BinarySearchTree):
    pass
