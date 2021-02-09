from .binary_search_trees import BinarySearchTree, BinarySearchTreeNode


class AVLTreeNode(BinarySearchTreeNode):
    def __init__(self, value):
        self.value = value
        self.height = 0

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"


class AVLTree(BinarySearchTree):
    @staticmethod
    def rotate_left(parent, direction, node_left, node_right):
        BinarySearchTree.rotate_left(parent, direction, node_left, node_right)
        node_left.height = max(
            AVLTree.height(node_left.right),
            AVLTree.height(node_left.left),
        ) + 1
        node_right.height = max(
            AVLTree.height(node_right.right),
            node_left.height,
        ) + 1

    @staticmethod
    def rotate_right(parent, direction, node_left, node_right):
        BinarySearchTree.rotate_right(parent, direction, node_left, node_right)
        node_right.height = max(
            AVLTree.height(node_right.right),
            AVLTree.height(node_right.left),
        ) + 1
        node_left.height = max(
            AVLTree.height(node_left.left),
            node_right.height,
        ) + 1

    @staticmethod
    def height(tree):
        if tree:
            return tree.height
        return -1

    @staticmethod
    def tree_add(tree, direction, value):
        node = getattr(tree, direction)
        if not node:
            setattr(tree, direction, AVLTreeNode(value))
            return getattr(tree, direction)

        if node.value < value:
            AVLTree.tree_add(node, "right", value)
            if AVLTree.height(node.right) - AVLTree.height(node.left) == 2:
                if value > node.right.value:
                    node = AVLTree.rotate_left(
                        tree, direction, node, node.right
                    )
                else:
                    node = AVLTree.rotate_right()
                    node = AVLTree.rotate_left()
        else:
            AVLTree.tree_add(node, "left", value)
            if AVLTree.height(node.left) - AVLTree.height(node.right) == 2:
                if value < node.left.value:
                    node = AVLTree.rotate_right(
                        tree, direction, node.left, node
                    )
                else:
                    node = AVLTree.rotate_left()
                    node = AVLTree.rotate_right()

        node = getattr(tree, direction)
        node.height = max(
            AVLTree.height(node.left),
            AVLTree.height(node.right),
        ) + 1

    def add(self, value):
        return AVLTree.tree_add(self, "root", value)
