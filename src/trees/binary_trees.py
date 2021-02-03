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
    def tree_add(tree, value):
        if tree.value < value:
            if tree.right is not None:
                return BinarySearchTree.tree_add(tree.right, value)
            tree.right = BinarySearchTreeNode(value)
        else:
            if tree.left is not None:
                return BinarySearchTree.tree_add(tree.left, value)
            tree.left = BinarySearchTreeNode(value)

    def add(self, value):
        return BinarySearchTree.tree_add(self.root, value)

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
