from trees.binary_trees import BinaryTree


def create_binary_tree():
    leaf = BinaryTree(1)
    leaf2 = BinaryTree(3)
    leaf3 = BinaryTree(5)
    leaf4 = BinaryTree(7)

    branch = BinaryTree(2)
    branch.left = leaf
    branch.right = leaf2

    branch2 = BinaryTree(6)
    branch2.left = leaf3
    branch2.left = leaf4

    root = BinaryTree(4)
    root.left = branch
    root.right = branch2
