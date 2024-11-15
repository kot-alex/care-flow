from typing import Optional, Any


class TreeNode:
    def __init__(self, data: Any):
        self.data = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.height = 1  # Height attribute for AVL balancing


class BinaryTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, data: Any) -> None:
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: TreeNode, data: Any) -> None:
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def inorder_traversal(self, node: Optional[TreeNode]) -> None:
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def search(self, data: Any) -> Optional[TreeNode]:
        return self._search_recursive(self.root, data)

    def _search_recursive(
        self, node: Optional[TreeNode], data: Any
    ) -> Optional[TreeNode]:
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)

    def is_empty(self) -> bool:
        return self.root is None


class BinarySearchTree(BinaryTree):
    def insert(self, data: Any) -> None:
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)


class AVLTree(BinarySearchTree):
    def insert(self, data: Any) -> None:
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: Optional[TreeNode], data: Any) -> TreeNode:
        # Perform normal BST insert
        if not node:
            return TreeNode(data)

        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        else:
            return node  # Duplicates are not allowed

        # Update height of the current node
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # Balance the node if unbalanced
        return self._balance_node(node)

    def _balance_node(self, node: TreeNode) -> TreeNode:
        balance = self._get_balance(node)

        # Left heavy
        if balance > 1:
            # Left-Right case
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            # Left-Left case
            return self._rotate_right(node)

        # Right heavy
        if balance < -1:
            # Right-Left case
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            # Right-Right case
            return self._rotate_left(node)

        return node  # The node is balanced

    def _rotate_left(self, node: TreeNode) -> TreeNode:
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        # Update heights after rotation
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(
            self._height(new_root.left), self._height(new_root.right)
        )

        return new_root

    def _rotate_right(self, node: TreeNode) -> TreeNode:
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        # Update heights after rotation
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(
            self._height(new_root.left), self._height(new_root.right)
        )

        return new_root

    def _get_balance(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return node.height
