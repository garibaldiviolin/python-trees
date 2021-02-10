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
    def test_tree_add_with_right_rotation(self, print_mock):
        AVLTree.tree_add(self.tree, "root", 0)
        AVLTree.tree_add(self.tree, "root", -1)
        AVLTree.tree_in_order_traversal(self.tree.root)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(-1, 8)]
        )

    @patch("builtins.print")
    def test_tree_add_with_left_right_rotations(self, print_mock):
        AVLTree.tree_add(self.tree, "root", -1)
        AVLTree.tree_add(self.tree, "root", 0)
        AVLTree.tree_in_order_traversal(self.tree.root)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(-1, 8)]
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

    @patch("builtins.print")
    def test_tree_add_with_left_rotation(self, print_mock):
        AVLTree.tree_add(self.tree, "root", 8)
        AVLTree.tree_add(self.tree, "root", 9)
        AVLTree.tree_in_order_traversal(self.tree.root)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 10)]
        )

    @patch("builtins.print")
    def test_tree_add_with_right_left_rotation(self, print_mock):
        AVLTree.tree_add(self.tree, "root", 9)
        AVLTree.tree_add(self.tree, "root", 8)
        AVLTree.tree_in_order_traversal(self.tree.root)
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 10)]
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


class TestAVLTreeRotateLeft(TestCase):
    def setUp(self):
        root_node = AVLTreeNode(4)
        root_node.height = 1
        root_node.right = AVLTreeNode(5)
        root_node.right.height = 0
        self.tree = AVLTree(root_node)

    @patch("builtins.print")
    def test_rotate_root_left(self, print_mock):
        left_node = self.tree.root
        right_node = self.tree.root.right

        AVLTree.rotate_left(
            self.tree,
            "root",
            left_node,
            right_node,
        )
        self.assertEqual(self.tree.root, right_node)
        self.assertEqual(self.tree.root.left, left_node)

        self.tree.in_order_traversal()
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(4, 6)]
        )

        self.assertEqual(self.tree.root.height, 1)
        self.assertEqual(self.tree.root.left.height, 0)


class TestAVLTreeRotateRight(TestCase):
    def setUp(self):
        root_node = AVLTreeNode(5)
        root_node.height = 1
        root_node.left = AVLTreeNode(4)
        root_node.left.height = 0
        self.tree = AVLTree(root_node)

    @patch("builtins.print")
    def test_rotate_root_right(self, print_mock):
        left_node = self.tree.root.left
        right_node = self.tree.root

        AVLTree.rotate_right(
            self.tree,
            "root",
            left_node,
            right_node,
        )
        self.assertEqual(self.tree.root, left_node)
        self.assertEqual(self.tree.root.right, right_node)

        self.tree.in_order_traversal()
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(4, 6)]
        )

        self.assertEqual(self.tree.root.height, 1)
        self.assertEqual(self.tree.root.right.height, 0)


class TestAVLTreeHeight(TestCase):
    def test_height(self):
        root = AVLTreeNode(3)
        root.height = 50
        tree = AVLTree(root)

        self.assertEqual(AVLTree.height(tree.root), 50)

    def test_height_with_null_node(self):
        tree = AVLTree(None)

        self.assertEqual(AVLTree.height(tree.root), -1)
