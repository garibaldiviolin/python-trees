class BinaryTreeNode:
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f"{self.__class__.__name__}({self.root.value})"

    def __str__(self):
        return str(self.root.value)

    @staticmethod
    def tree_in_order_traversal(tree):
        if tree.left is not None:
            BinaryTree.tree_in_order_traversal(tree.left)

        print(tree.value, end="-")

        if tree.right is not None:
            BinaryTree.tree_in_order_traversal(tree.right)

    def in_order_traversal(self):
        BinaryTree.tree_in_order_traversal(self.root)

    @staticmethod
    def tree_pre_order_traversal(tree):
        print(tree.value, end="-")

        if tree.left is not None:
            BinaryTree.tree_pre_order_traversal(tree.left)

        if tree.right is not None:
            BinaryTree.tree_pre_order_traversal(tree.right)

    def pre_order_traversal(self):
        BinaryTree.tree_pre_order_traversal(self.root)

    @staticmethod
    def tree_post_order_traversal(tree):
        if tree.left is not None:
            BinaryTree.tree_post_order_traversal(tree.left)

        if tree.right is not None:
            BinaryTree.tree_post_order_traversal(tree.right)

        print(tree.value, end="-")

    def post_order_traversal(self):
        BinaryTree.tree_post_order_traversal(self.root)

    @staticmethod
    def binary_tree_search(tree, direction, value):
        sub_tree = getattr(tree, direction)
        if sub_tree.value == value:
            return True, tree, direction
        if sub_tree.value < value and sub_tree.right is not None:
            return BinaryTree.binary_tree_search(sub_tree, "right", value)
        elif sub_tree.value > value and sub_tree.left is not None:
            return BinaryTree.binary_tree_search(sub_tree, "left", value)

        return False, None, None

    def search(self, value):
        return BinaryTree.binary_tree_search(self, "root", value)

    @staticmethod
    def tree_add(tree, value):
        if tree.value < value:
            if tree.right is not None:
                return BinaryTree.tree_add(tree.right, value)
            tree.right = BinaryTreeNode(value)
        else:
            if tree.left is not None:
                return BinaryTree.tree_add(tree.left, value)
            tree.left = BinaryTreeNode(value)

    def add(self, value):
        return BinaryTree.tree_add(self.root, value)

    @staticmethod
    def tree_max_value(tree):
        if tree.right is not None:
            return BinaryTree.tree_max_value(tree.right)
        return tree

    def max_value(self):
        return BinaryTree.tree_max_value(self.root)

    def remove(self, value):
        parent = self
        current_node = self.root
        direction = "root"
        while current_node and current_node.value != value:
            parent = current_node
            if current_node.value > value:
                current_node = current_node.left
                direction = "left"
            else:
                current_node = current_node.right
                direction = "right"

        if not current_node:
            return False

        if not current_node.left:
            setattr(parent, direction, current_node.right)
        elif not current_node.right:
            setattr(parent, direction, current_node.left)
        else:
            in_order_successor = current_node.left
            successor_parent = current_node
            successor_parent_direction = "left"
            while in_order_successor.right:
                successor_parent = in_order_successor
                in_order_successor = in_order_successor.right
                successor_parent_direction = "right"
            current_node.value = in_order_successor.value

            setattr(
                successor_parent,
                successor_parent_direction,
                in_order_successor.left
            )
        return True
