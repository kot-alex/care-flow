import unittest
from unittest.mock import patch
from data_structures.binary_tree import BinaryTree, BinarySearchTree, AVLTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = BinaryTree()
        self.bst = BinarySearchTree()
        self.avl = AVLTree()

    @patch("builtins.print")  # Capture print output
    def test_binary_tree_insert_and_traversal(self, mock_print):
        self.bt.insert(10)
        self.bt.insert(5)
        self.bt.insert(15)
        self.bt.inorder_traversal(self.bt.root)
        mock_print.assert_any_call(5, end=" ")
        mock_print.assert_any_call(10, end=" ")
        mock_print.assert_any_call(15, end=" ")

    def test_bst_insert_and_search(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertIsNotNone(self.bst.search(5))
        self.assertIsNone(self.bst.search(100))

    def test_avl_search(self):
        self.avl.insert(10)
        self.avl.insert(20)
        self.avl.insert(30)
        self.assertTrue(self.avl.search(20))
        self.assertFalse(self.avl.search(100))

    def test_is_empty(self):
        self.assertTrue(self.avl.is_empty())
        self.avl.insert(1)
        self.assertFalse(self.avl.is_empty())


if __name__ == "__main__":
    unittest.main()
