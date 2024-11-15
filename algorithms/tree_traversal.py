class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeTraversal:
    @staticmethod
    def in_order(node):
        result = []
        TreeTraversal._in_order_helper(node, result)
        return result

    @staticmethod
    def _in_order_helper(node, result):
        if node:
            TreeTraversal._in_order_helper(node.left, result)  # Traverse left subtree
            if node.data is not None:
                result.append(node.data)  # Append node data to result list
            TreeTraversal._in_order_helper(node.right, result)  # Traverse right subtree

    @staticmethod
    def pre_order(node):
        result = []
        TreeTraversal._pre_order_helper(node, result)
        return result

    @staticmethod
    def _pre_order_helper(node, result):
        if node:
            if node.data is not None:
                result.append(node.data)  # Append node data to result list
            TreeTraversal._pre_order_helper(node.left, result)  # Traverse left subtree
            TreeTraversal._pre_order_helper(
                node.right, result
            )  # Traverse right subtree

    @staticmethod
    def post_order(node):
        result = []
        TreeTraversal._post_order_helper(node, result)
        return result

    @staticmethod
    def _post_order_helper(node, result):
        if node:
            TreeTraversal._post_order_helper(node.left, result)  # Traverse left subtree
            TreeTraversal._post_order_helper(
                node.right, result
            )  # Traverse right subtree
            if node.data is not None:
                result.append(node.data)  # Append node data to result list
