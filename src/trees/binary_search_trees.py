class BinarySearchTreeNode:
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f"{self.__class__.__name__}({self.root.value})"

    def __str__(self):
        return str(self.root.value)

    @staticmethod
    def tree_in_order_traversal(tree):
        if tree.left is not None:
            BinarySearchTree.tree_in_order_traversal(tree.left)

        print(tree.value, end="-")

        if tree.right is not None:
            BinarySearchTree.tree_in_order_traversal(tree.right)

    def in_order_traversal(self):
        BinarySearchTree.tree_in_order_traversal(self.root)

    @staticmethod
    def tree_pre_order_traversal(tree):
        print(tree.value, end="-")

        if tree.left is not None:
            BinarySearchTree.tree_pre_order_traversal(tree.left)

        if tree.right is not None:
            BinarySearchTree.tree_pre_order_traversal(tree.right)

    def pre_order_traversal(self):
        BinarySearchTree.tree_pre_order_traversal(self.root)

    @staticmethod
    def tree_post_order_traversal(tree):
        if tree.left is not None:
            BinarySearchTree.tree_post_order_traversal(tree.left)

        if tree.right is not None:
            BinarySearchTree.tree_post_order_traversal(tree.right)

        print(tree.value, end="-")

    def post_order_traversal(self):
        BinarySearchTree.tree_post_order_traversal(self.root)

    def tree_print(node, identifier, level):
        element = f"{identifier}{node.value}"
        spaces = 0 if level < 2 else len(element) - 1 + level * 2
        print(f"{element:>{spaces}}")
        if node.left:
            BinarySearchTree.tree_print(node.left, "|-L:", level + 1)
        if node.right:
            BinarySearchTree.tree_print(node.right, "|-R:", level + 1)

    def print(self):
        BinarySearchTree.tree_print(self.root, "", 0)

    @staticmethod
    def binary_tree_search(tree, direction, value):
        sub_tree = getattr(tree, direction)
        if sub_tree.value == value:
            return True, tree, direction
        if sub_tree.value < value and sub_tree.right is not None:
            return BinarySearchTree.binary_tree_search(
                sub_tree,
                "right",
                value,
            )
        elif sub_tree.value > value and sub_tree.left is not None:
            return BinarySearchTree.binary_tree_search(sub_tree, "left", value)

        return False, None, None

    def search(self, value):
        return BinarySearchTree.binary_tree_search(self, "root", value)

    @staticmethod
    def tree_add(tree, direction, value):
        node = getattr(tree, direction)
        if not node:
            setattr(tree, direction, BinarySearchTreeNode(value))
            return

        if node.value < value:
            return BinarySearchTree.tree_add(node, "right", value)
        else:
            return BinarySearchTree.tree_add(node, "left", value)

    def add(self, value):
        return BinarySearchTree.tree_add(self, "root", value)

    @staticmethod
    def tree_max_value(parent, direction):
        node = getattr(parent, direction)
        while node.right:
            parent = node
            node = node.right
            direction = "right"

        return parent, direction, node

    def max_value(self):
        return BinarySearchTree.tree_max_value(self, "root")

    def remove(self, value):
        found, parent, direction = self.search(value)

        if not found:
            return False

        current_node = getattr(parent, direction)
        if not current_node.left:
            setattr(parent, direction, current_node.right)
        elif not current_node.right:
            setattr(parent, direction, current_node.left)
        else:
            parent, direction, successor = BinarySearchTree.tree_max_value(
                current_node, "left"
            )
            current_node.value = successor.value
            setattr(parent, direction, successor.left)
        return True

    def rotate_left(self, parent, direction, node_left, node_right):
        node_left.right = node_right.left
        node_right.left = node_left
        setattr(parent, direction, node_right)

    def rotate_right(self, parent, direction, node_left, node_right):
        node_right.left = node_left.right
        node_left.right = node_right
        setattr(parent, direction, node_left)
