import unittest
from algorithms.tree_traversal import TreeTraversal


class TestTreeTraversal(unittest.TestCase):

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    class TreeTraversal:
        @staticmethod
        def in_order(node):
            result = []
            if node:
                result.extend(TreeTraversal.in_order(node.left))
                result.append(node.data)
                result.extend(TreeTraversal.in_order(node.right))
            return result

        @staticmethod
        def pre_order(node):
            result = []
            if node:
                result.append(node.data)
                result.extend(TreeTraversal.pre_order(node.left))
                result.extend(TreeTraversal.pre_order(node.right))
            return result

        @staticmethod
        def post_order(node):
            result = []
            if node:
                result.extend(TreeTraversal.post_order(node.left))
                result.extend(TreeTraversal.post_order(node.right))
                result.append(node.data)
            return result

    def setUp(self):
        # Create a simple binary tree for testing
        self.root = self.TreeNode(1)
        self.root.left = self.TreeNode(2)
        self.root.right = self.TreeNode(3)
        self.root.left.left = self.TreeNode(4)
        self.root.left.right = self.TreeNode(5)

    def test_in_order(self):
        expected = [4, 2, 5, 1, 3]
        result = self.TreeTraversal.in_order(self.root)
        self.assertEqual(result, expected)

    def test_pre_order(self):
        expected = [1, 2, 4, 5, 3]
        result = self.TreeTraversal.pre_order(self.root)
        self.assertEqual(result, expected)

    def test_post_order(self):
        expected = [4, 5, 2, 3, 1]
        result = self.TreeTraversal.post_order(self.root)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
