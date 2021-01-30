from trees.binary_trees import BinaryTree, BinaryTreeNode


def create_binary_tree():
    leaf = BinaryTreeNode(1)
    leaf2 = BinaryTreeNode(3)
    leaf3 = BinaryTreeNode(5)
    leaf4 = BinaryTreeNode(7)

    branch = BinaryTreeNode(2)
    branch.left = leaf
    branch.right = leaf2

    branch2 = BinaryTreeNode(6)
    branch2.left = leaf3
    branch2.right = leaf4

    root = BinaryTreeNode(4)
    root.left = branch
    root.right = branch2

    tree = BinaryTree(root)

    return tree
