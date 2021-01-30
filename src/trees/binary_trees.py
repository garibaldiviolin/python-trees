class BinaryTree:
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def __str__(self):
        return str(self.value)


def in_order_traversal(tree):
    if tree.left is not None:
        in_order_traversal(tree.left)

    print(tree.value, end="-")

    if tree.right is not None:
        in_order_traversal(tree.right)


def pre_order_traversal(tree):
    print(tree.value, end="-")

    if tree.left is not None:
        pre_order_traversal(tree.left)

    if tree.right is not None:
        pre_order_traversal(tree.right)


def post_order_traversal(tree):
    if tree.left is not None:
        post_order_traversal(tree.left)

    if tree.right is not None:
        post_order_traversal(tree.right)

    print(tree.value, end="-")


def binary_tree_search(tree, value):
    if tree.value == value:
        return True
    if tree.value < value and tree.right is not None:
        return binary_tree_search(tree.right, value)
    elif tree.value > value and tree.left is not None:
        return binary_tree_search(tree.left, value)

    return False
