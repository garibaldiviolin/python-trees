from unittest import TestCase

from trees.avl_trees import AVLTree, AVLTreeNode

from .fixtures import create_avl_tree
from .test_binary_search_trees import (
    TestBinarySearchTreeNodeClass,
    TestBinarySearchTreeClass,
    TestBinarySearchTreeTraversal,
    TestBinarySearchTreePrint,
    TestBinarySearchTreeSearch,
    TestBinarySearchTreeAdd,
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


class TestAVLTreeAdd(TestBinarySearchTreeAdd):
    def setUp(self):
        self.tree = create_avl_tree()


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
