from unittest import TestCase
from unittest.mock import call, patch

from .fixtures import create_binary_tree
from trees.binary_trees import (
    BinaryTree,
    post_order_traversal,
    pre_order_traversal,
    in_order_traversal,
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
        self.assertEqual(repr(self.binary_tree), "BinaryTree(2)")


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
