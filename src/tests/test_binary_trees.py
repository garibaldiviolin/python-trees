from unittest import TestCase
from unittest.mock import call, patch

from .fixtures import create_binary_tree
from trees.binary_trees import (
    BinaryTree,
    post_order_traversal,
    pre_order_traversal,
    in_order_traversal,
    binary_tree_search,
    tree_add,
)


class TestBinaryTreeClass(TestCase):
    def setUp(self):
        self.binary_tree = BinaryTree(2)

    def test_instance(self):
        self.assertIsNone(self.binary_tree.left)
        self.assertIsNone(self.binary_tree.right)
        self.assertEqual(self.binary_tree.value, 2)

    def test_repr(self):
        self.assertEqual(repr(self.binary_tree), "BinaryTree(2)")

    def test_str(self):
        self.assertEqual(str(self.binary_tree), "2")


class TestBinaryTreeTraversal(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    @patch("builtins.print")
    def test_post_order_traversal(self, print_mock):
        post_order_traversal(self.binary_tree)
        values_order = [1, 3, 2, 5, 7, 6, 4]
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in values_order]
        )

    @patch("builtins.print")
    def test_pre_order_traversal(self, print_mock):
        pre_order_traversal(self.binary_tree)
        values_order = [4, 2, 1, 3, 6, 5, 7]
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in values_order]
        )

    @patch("builtins.print")
    def test_in_order_traversal(self, print_mock):
        in_order_traversal(self.binary_tree)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 8)]
        )


class TestBinaryTreeSearch(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    def test_binary_tree_search_with_existing_value(self):
        found = binary_tree_search(self.binary_tree, 1)
        self.assertTrue(found)

    def test_binary_tree_search_with_inexistent_value(self):
        self.binary_tree.right.right.value = 8  # replace 7 to test
        found = binary_tree_search(self.binary_tree, 7)
        self.assertFalse(found)


class TestBinaryTreeAdd(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    @patch("builtins.print")
    def test_add_left(self, print_mock):
        self.binary_tree.right.right.value = 8  # replace 7 to test
        tree_add(self.binary_tree, 7)
        in_order_traversal(self.binary_tree)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 9)]
        )

    @patch("builtins.print")
    def test_add_right(self, print_mock):
        self.binary_tree.left.left.value = 0  # replace 1 to test
        tree_add(self.binary_tree, 1)
        in_order_traversal(self.binary_tree)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(0, 8)]
        )
