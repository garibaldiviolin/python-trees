from unittest import TestCase
from unittest.mock import call, patch

from .fixtures import create_binary_tree
from trees.binary_search_trees import BinarySearchTree, BinarySearchTreeNode


class TestBinarySearchTreeNodeClass(TestCase):
    def setUp(self):
        self.binary_tree = BinarySearchTreeNode(2)

    def test_instance(self):
        self.assertIsNone(self.binary_tree.left)
        self.assertIsNone(self.binary_tree.right)
        self.assertEqual(self.binary_tree.value, 2)

    def test_repr(self):
        self.assertEqual(repr(self.binary_tree), "BinarySearchTreeNode(2)")

    def test_str(self):
        self.assertEqual(str(self.binary_tree), "2")


class TestBinarySearchTreeClass(TestCase):
    def setUp(self):
        self.binary_tree_node = BinarySearchTreeNode(2)
        self.binary_tree = BinarySearchTree(self.binary_tree_node)

    def test_instance(self):
        self.assertEqual(self.binary_tree.root, self.binary_tree_node)

    def test_repr(self):
        self.assertEqual(repr(self.binary_tree), "BinarySearchTree(2)")

    def test_str(self):
        self.assertEqual(str(self.binary_tree), "2")


class TestBinarySearchTreeTraversal(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    @patch("builtins.print")
    def test_post_order_traversal(self, print_mock):
        BinarySearchTree.tree_post_order_traversal(self.binary_tree.root)
        values_order = [1, 3, 2, 5, 7, 6, 4]
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in values_order]
        )

    @patch(
        "trees.binary_search_trees.BinarySearchTree.tree_post_order_traversal"
    )
    def test_tree_post_order_traversal(self, tree_post_order_traversal_mock):
        self.binary_tree.post_order_traversal()
        tree_post_order_traversal_mock.assert_called_once_with(
            self.binary_tree.root
        )

    @patch("builtins.print")
    def test_pre_order_traversal(self, print_mock):
        BinarySearchTree.tree_pre_order_traversal(self.binary_tree.root)
        values_order = [4, 2, 1, 3, 6, 5, 7]
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in values_order]
        )

    @patch(
        "trees.binary_search_trees.BinarySearchTree.tree_pre_order_traversal"
    )
    def test_tree_pre_order_traversal(self, tree_pre_order_traversal_mock):
        self.binary_tree.pre_order_traversal()
        tree_pre_order_traversal_mock.assert_called_once_with(
            self.binary_tree.root
        )

    @patch("builtins.print")
    def test_in_order_traversal(self, print_mock):
        BinarySearchTree.tree_in_order_traversal(self.binary_tree.root)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 8)]
        )

    @patch(
        "trees.binary_search_trees.BinarySearchTree.tree_in_order_traversal"
    )
    def test_tree_in_order_traversal(self, tree_in_order_traversal_mock):
        self.binary_tree.in_order_traversal()
        tree_in_order_traversal_mock.assert_called_once_with(
            self.binary_tree.root
        )


class TestBinarySearchTreePrint(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    @patch("builtins.print")
    def test_tree_print(self, print_mock):
        BinarySearchTree.tree_print(
            self.binary_tree.root,
            "",
            0
        )
        self.assertEqual(print_mock.mock_calls, [
            call("4"),
            call("|-L:2"),
            call("   |-L:1"),
            call("   |-R:3"),
            call("|-R:6"),
            call("   |-L:5"),
            call("   |-R:7"),
        ])

    @patch("trees.binary_search_trees.BinarySearchTree.tree_print")
    def test_print(self, tree_print_mock):
        self.binary_tree.print()
        tree_print_mock.assert_called_once_with(
            self.binary_tree.root, "", 0
        )


class TestBinarySearchTreeSearch(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    def test_binary_tree_search_in_left_subtree(self):
        expected_leaf = self.binary_tree.root.left
        found, parent, direction = BinarySearchTree.binary_tree_search(
            self.binary_tree,
            "root",
            1,
        )
        found_node = getattr(parent, direction)
        self.assertEqual(
            (found, parent, direction),
            (True, expected_leaf, "left")
        )
        self.assertEqual(found_node.value, 1)

    def test_binary_tree_search_in_right_subtree(self):
        expected_leaf = self.binary_tree.root.right
        found, parent, direction = BinarySearchTree.binary_tree_search(
            self.binary_tree,
            "root",
            7,
        )
        found_node = getattr(parent, direction)
        self.assertEqual(
            (found, parent, direction),
            (True, expected_leaf, "right")
        )
        self.assertEqual(found_node.value, 7)

    def test_binary_tree_search_with_inexistent_value(self):
        self.binary_tree.root.right.right.value = 8  # replace 7 to test
        found, parent, direction = BinarySearchTree.binary_tree_search(
            self.binary_tree,
            "root",
            7,
        )
        self.assertEqual((found, parent, direction), (False, None, None))

    @patch("trees.binary_search_trees.BinarySearchTree.binary_tree_search")
    def test_search(self, binary_tree_search_mock):
        self.binary_tree.search(7)
        binary_tree_search_mock.assert_called_once_with(
            self.binary_tree, "root", 7
        )


class TestBinarySearchTreeAdd(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    @patch("builtins.print")
    def test_tree_add_left(self, print_mock):
        self.binary_tree.root.right.right.value = 8  # replace 7 to test
        BinarySearchTree.tree_add(self.binary_tree.root, 7)
        BinarySearchTree.tree_in_order_traversal(self.binary_tree.root)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 9)]
        )

    @patch("builtins.print")
    def test_tree_add_right(self, print_mock):
        self.binary_tree.root.left.left.value = 0  # replace 1 to test
        BinarySearchTree.tree_add(self.binary_tree.root, 1)
        BinarySearchTree.tree_in_order_traversal(self.binary_tree.root)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(0, 8)]
        )

    @patch("trees.binary_search_trees.BinarySearchTree.tree_add")
    def test_search(self, tree_add_mock):
        self.binary_tree.add(7)
        tree_add_mock.assert_called_once_with(self.binary_tree.root, 7)


class TestBinarySearchTreeMaxValue(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    def test_tree_max_value(self):
        parent, direction, node = BinarySearchTree.tree_max_value(
            self.binary_tree, "root"
        )
        self.assertEqual(parent, self.binary_tree.root.right)
        self.assertEqual(direction, "right")
        self.assertEqual(node.value, 7)

    def test_tree_max_value_with_single_value(self):
        single_value_tree = BinarySearchTree(BinarySearchTreeNode(50))
        parent, direction, node = BinarySearchTree.tree_max_value(
            single_value_tree,
            "root",
        )
        self.assertEqual(parent, single_value_tree)
        self.assertEqual(direction, "root")
        self.assertEqual(node.value, 50)

    @patch("trees.binary_search_trees.BinarySearchTree.tree_max_value")
    def test_max_value(self, tree_max_value_mock):
        expected_return_value = BinarySearchTree(463)
        tree_max_value_mock.return_value = expected_return_value
        return_value = self.binary_tree.max_value()

        self.assertEqual(expected_return_value, return_value)
        tree_max_value_mock.assert_called_once_with(
            self.binary_tree,
            "root"
        )


class TestBinarySearchTreeRemove(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    def test_remove_value_not_found(self):
        removed = self.binary_tree.remove(1000)
        self.assertFalse(removed)

    def test_remove_single_node_tree(self):
        root = BinarySearchTreeNode(50)
        binary_tree = BinarySearchTree(root)
        binary_tree.remove(50)
        self.assertIsNone(binary_tree.root)

    @patch("builtins.print")
    def test_remove_node_without_children(self, print_mock):
        self.binary_tree.remove(1)
        self.binary_tree.in_order_traversal()
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(2, 8)]
        )

    @patch("builtins.print")
    def test_remove_node_with_only_left_child(self, print_mock):
        self.binary_tree.root.left.right = None  # Remove value 3
        self.binary_tree.remove(2)
        self.binary_tree.in_order_traversal()
        self.assertEqual(
            print_mock.mock_calls,
            [
                call(number, end="-") for number in range(1, 8)
                if number not in (2, 3)
            ]
        )

    @patch("builtins.print")
    def test_remove_node_with_only_right_child(self, print_mock):
        self.binary_tree.root.left.left = None  # Remove value 1
        self.binary_tree.remove(2)
        self.binary_tree.in_order_traversal()
        self.assertEqual(
            print_mock.mock_calls,
            [
                call(number, end="-") for number in range(1, 8)
                if number not in (1, 2)
            ]
        )

    @patch("builtins.print")
    def test_remove_node_with_both_children(self, print_mock):
        self.binary_tree.remove(4)
        self.binary_tree.in_order_traversal()
        self.assertEqual(
            print_mock.mock_calls,
            [
                call(number, end="-") for number in range(1, 8)
                if number != 4
            ]
        )


class TestBinarySearchTreeRotateLeft(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    @patch("builtins.print")
    def test_rotate_root_left(self, print_mock):
        left_node = self.binary_tree.root
        right_node = self.binary_tree.root.right

        self.binary_tree.rotate_left(
            self.binary_tree,
            "root",
            left_node,
            right_node,
        )
        self.assertEqual(self.binary_tree.root, right_node)
        self.assertEqual(self.binary_tree.root.left, left_node)

        self.binary_tree.in_order_traversal()
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 8)]
        )


class TestBinarySearchTreeRotateRight(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    @patch("builtins.print")
    def test_rotate_root_right(self, print_mock):
        left_node = self.binary_tree.root.left
        right_node = self.binary_tree.root

        self.binary_tree.rotate_right(
            self.binary_tree,
            "root",
            left_node,
            right_node,
        )
        self.assertEqual(self.binary_tree.root, left_node)
        self.assertEqual(self.binary_tree.root.right, right_node)

        self.binary_tree.in_order_traversal()
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 8)]
        )
