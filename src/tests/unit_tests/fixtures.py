from trees.binary_search_trees import BinarySearchTree, BinarySearchTreeNode
from trees.avl_trees import AVLTree, AVLTreeNode


def create_binary_search_tree():
    leaf = BinarySearchTreeNode(1)
    leaf2 = BinarySearchTreeNode(3)
    leaf3 = BinarySearchTreeNode(5)
    leaf4 = BinarySearchTreeNode(7)

    branch = BinarySearchTreeNode(2)
    branch.left = leaf
    branch.right = leaf2

    branch2 = BinarySearchTreeNode(6)
    branch2.left = leaf3
    branch2.right = leaf4

    root = BinarySearchTreeNode(4)
    root.left = branch
    root.right = branch2

    tree = BinarySearchTree(root)

    return tree


def create_avl_tree():
    leaf = AVLTreeNode(1)
    leaf2 = AVLTreeNode(3)
    leaf3 = AVLTreeNode(5)
    leaf4 = AVLTreeNode(7)

    branch = AVLTreeNode(2)
    branch.left = leaf
    branch.right = leaf2

    branch2 = AVLTreeNode(6)
    branch2.left = leaf3
    branch2.right = leaf4

    root = AVLTreeNode(4)
    root.left = branch
    root.right = branch2

    tree = AVLTree(root)

    return tree
