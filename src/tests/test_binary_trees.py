from unittest import TestCase

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
        self.assertEqual(repr(self.binary_tree), "BinaryTree(2)")
