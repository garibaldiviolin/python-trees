from unittest import TestCase
from unittest.mock import call, patch

from trees.avl_trees import AVLTree, AVLTreeNode

from .fixtures import create_avl_tree
from .test_binary_search_trees import (
    TestBinarySearchTreeClass,
    TestBinarySearchTreeTraversal,
    TestBinarySearchTreePrint,
    TestBinarySearchTreeSearch,
    TestBinarySearchTreeMaxValue,
    TestBinarySearchTreeRemove,
    TestBinarySearchTreeRotateLeft,
    TestBinarySearchTreeRotateRight,
)


class TestAVLTreeNodeClass(TestCase):
    def setUp(self):
        self.tree_node = AVLTreeNode(2)

    def test_instance(self):
        self.assertIsNone(self.tree_node.left)
        self.assertIsNone(self.tree_node.right)
        self.assertEqual(self.tree_node.height, 0)
        self.assertEqual(self.tree_node.value, 2)

    def test_repr(self):
        self.assertEqual(repr(self.tree_node), "AVLTreeNode(2)")

    def test_str(self):
        self.assertEqual(str(self.tree_node), "2")


class TestAVLTreeClass(TestBinarySearchTreeClass):
    def setUp(self):
        self.tree_node = AVLTreeNode(2)
        self.tree = AVLTree(self.tree_node)

    def test_repr(self):
        self.assertEqual(repr(self.tree), "AVLTree(2)")


class TestAVLTreeTraversal(TestBinarySearchTreeTraversal):
    def setUp(self):
        self.tree = create_avl_tree()


class TestAVLTreePrint(TestBinarySearchTreePrint):
    def setUp(self):
        self.tree = create_avl_tree()


class TestAVLTreeSearch(TestBinarySearchTreeSearch):
    def setUp(self):
        self.tree = create_avl_tree()


class TestAVLTreeAdd(TestCase):
    def setUp(self):
        self.tree = create_avl_tree()

    @patch("builtins.print")
    def test_tree_add_left(self, print_mock):
        self.tree.root.right.right.value = 8  # replace 7 to test
        AVLTree.tree_add(self.tree, "root", 7)
        AVLTree.tree_in_order_traversal(self.tree.root)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 9)]
        )

    @patch("builtins.print")
    def test_tree_add_right(self, print_mock):
        self.tree.root.left.left.value = 0  # replace 1 to test
        AVLTree.tree_add(self.tree, "root", 1)
        AVLTree.tree_in_order_traversal(self.tree.root)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(0, 8)]
        )

    @patch("trees.avl_trees.AVLTree.tree_add")
    def test_add(self, tree_add_mock):
        self.tree.add(7)
        tree_add_mock.assert_called_once_with(self.tree, "root", 7)


class TestAVLTreeMaxValue(TestBinarySearchTreeMaxValue):
    def setUp(self):
        self.tree = create_avl_tree()


class TestAVLTreeRemove(TestBinarySearchTreeRemove):
    def setUp(self):
        self.tree = create_avl_tree()


class TestAVLTreeRotateLeft(TestBinarySearchTreeRotateLeft):
    def setUp(self):
        self.tree = create_avl_tree()


class TestAVLTreeRotateRight(TestBinarySearchTreeRotateRight):
    def setUp(self):
        self.tree = create_avl_tree()
