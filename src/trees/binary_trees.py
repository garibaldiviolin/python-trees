class BinaryTree:
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def __str__(self):
        return str(self.value)

    @staticmethod
    def tree_in_order_traversal(tree):
        if tree.left is not None:
            BinaryTree.tree_in_order_traversal(tree.left)

        print(tree.value, end="-")

        if tree.right is not None:
            BinaryTree.tree_in_order_traversal(tree.right)

    def in_order_traversal(self):
        BinaryTree.tree_in_order_traversal(self)

    @staticmethod
    def tree_pre_order_traversal(tree):
        print(tree.value, end="-")

        if tree.left is not None:
            BinaryTree.tree_pre_order_traversal(tree.left)

        if tree.right is not None:
            BinaryTree.tree_pre_order_traversal(tree.right)

    def pre_order_traversal(self):
        BinaryTree.tree_pre_order_traversal(self)

    @staticmethod
    def tree_post_order_traversal(tree):
        if tree.left is not None:
            BinaryTree.tree_post_order_traversal(tree.left)

        if tree.right is not None:
            BinaryTree.tree_post_order_traversal(tree.right)

        print(tree.value, end="-")

    def post_order_traversal(self):
        BinaryTree.tree_post_order_traversal(self)

    @staticmethod
    def binary_tree_search(tree, value):
        if tree.value == value:
            return True, tree
        if tree.value < value and tree.right is not None:
            return BinaryTree.binary_tree_search(tree.right, value)
        elif tree.value > value and tree.left is not None:
            return BinaryTree.binary_tree_search(tree.left, value)

        return False, None

    def search(self, value):
        return BinaryTree.binary_tree_search(self, value)

    @staticmethod
    def tree_add(tree, value):
        if tree.value < value:
            if tree.right is not None:
                return BinaryTree.tree_add(tree.right, value)
            tree.right = BinaryTree(value)
        else:
            if tree.left is not None:
                return BinaryTree.tree_add(tree.left, value)
            tree.left = BinaryTree(value)

    def add(self, value):
        return BinaryTree.tree_add(self, value)

    @staticmethod
    def tree_max_value(tree):
        if tree.right is not None:
            return BinaryTree.tree_max_value(tree.right)
        return tree

    def max_value(self):
        return BinaryTree.tree_max_value(self)
