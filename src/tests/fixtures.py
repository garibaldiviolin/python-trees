from trees.binary_search_trees import BinarySearchTree, BinarySearchTreeNode


def create_binary_tree():
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
