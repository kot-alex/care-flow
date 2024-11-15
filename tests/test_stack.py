import unittest
from data_structures.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.size(), 3)  # Stack should have 3 elements

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(
            self.stack.pop(), 30
        )  # Last element added is the first to be popped
        self.assertEqual(self.stack.size(), 2)  # Stack should now have 2 elements

    def test_peek(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)  # The top element is 20
        self.assertEqual(self.stack.size(), 2)  # Size should remain the same

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())  # Stack should be empty initially
        self.stack.push(10)
        self.assertFalse(
            self.stack.is_empty()
        )  # Stack should not be empty after pushing an element
        self.stack.pop()
        self.assertTrue(
            self.stack.is_empty()
        )  # Stack should be empty after popping the last element

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)  # Initially, stack size should be 0
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(
            self.stack.size(), 2
        )  # Size should be 2 after pushing 2 elements

    def test_pop_empty_stack(self):
        self.assertIsNone(
            self.stack.pop()
        )  # Popping from an empty stack should return None

    def test_peek_empty_stack(self):
        self.assertIsNone(
            self.stack.peek()
        )  # Peeking at an empty stack should return None


if __name__ == "__main__":
    unittest.main()
