from unittest import TestCase
from unittest.mock import call, patch

from .fixtures import create_binary_tree
from trees.binary_trees import BinaryTree


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
        BinaryTree.post_order_traversal(self.binary_tree)
        values_order = [1, 3, 2, 5, 7, 6, 4]
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in values_order]
        )

    @patch("trees.binary_trees.BinaryTree.tree_post_order_traversal")
    def test_tree_post_order_traversal(self, tree_post_order_traversal_mock):
        self.binary_tree.post_order_traversal()
        tree_post_order_traversal_mock.assert_called_once_with(
            self.binary_tree
        )

    @patch("builtins.print")
    def test_pre_order_traversal(self, print_mock):
        BinaryTree.tree_pre_order_traversal(self.binary_tree)
        values_order = [4, 2, 1, 3, 6, 5, 7]
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in values_order]
        )

    @patch("trees.binary_trees.BinaryTree.tree_pre_order_traversal")
    def test_tree_pre_order_traversal(self, tree_pre_order_traversal_mock):
        self.binary_tree.pre_order_traversal()
        tree_pre_order_traversal_mock.assert_called_once_with(
            self.binary_tree
        )

    @patch("builtins.print")
    def test_in_order_traversal(self, print_mock):
        BinaryTree.tree_in_order_traversal(self.binary_tree)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 8)]
        )

    @patch("trees.binary_trees.BinaryTree.tree_in_order_traversal")
    def test_tree_in_order_traversal(self, tree_in_order_traversal_mock):
        self.binary_tree.in_order_traversal()
        tree_in_order_traversal_mock.assert_called_once_with(
            self.binary_tree
        )


class TestBinaryTreeSearch(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    def test_binary_tree_search_with_existing_value(self):
        found = BinaryTree.binary_tree_search(self.binary_tree, 1)
        self.assertTrue(found)

    def test_binary_tree_search_with_inexistent_value(self):
        self.binary_tree.right.right.value = 8  # replace 7 to test
        found = BinaryTree.binary_tree_search(self.binary_tree, 7)
        self.assertFalse(found)

    @patch("trees.binary_trees.BinaryTree.binary_tree_search")
    def test_search(self, binary_tree_search_mock):
        self.binary_tree.search(7)
        binary_tree_search_mock.assert_called_once_with(self.binary_tree, 7)


class TestBinaryTreeAdd(TestCase):
    def setUp(self):
        self.binary_tree = create_binary_tree()

    @patch("builtins.print")
    def test_tree_add_left(self, print_mock):
        self.binary_tree.right.right.value = 8  # replace 7 to test
        BinaryTree.tree_add(self.binary_tree, 7)
        BinaryTree.tree_in_order_traversal(self.binary_tree)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 9)]
        )

    @patch("builtins.print")
    def test_tree_add_right(self, print_mock):
        self.binary_tree.left.left.value = 0  # replace 1 to test
        BinaryTree.tree_add(self.binary_tree, 1)
        BinaryTree.tree_in_order_traversal(self.binary_tree)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(0, 8)]
        )

    @patch("trees.binary_trees.BinaryTree.tree_add")
    def test_search(self, tree_add_mock):
        self.binary_tree.add(7)
        tree_add_mock.assert_called_once_with(self.binary_tree, 7)
