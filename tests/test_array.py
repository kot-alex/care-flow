import unittest
from data_structures.array import Array


class TestArray(unittest.TestCase):

    def setUp(self):
        self.array = Array()

    def test_append(self):
        self.array.append(10)
        self.array.append(20)
        self.assertEqual(self.array.size(), 2)

    def test_insert(self):
        self.array.append(10)
        self.array.insert(1, 15)
        self.assertEqual(self.array.get(1), 15)

    def test_remove(self):
        self.array.append(10)
        self.array.append(20)
        self.array.remove(10)
        self.assertEqual(self.array.size(), 1)

    def test_pop(self):
        self.array.append(10)
        self.assertEqual(self.array.pop(), 10)
        self.assertEqual(self.array.size(), 0)

    def test_get(self):
        self.array.append(10)
        self.assertEqual(self.array.get(0), 10)

    def test_set(self):
        self.array.append(10)
        self.array.set(0, 20)
        self.assertEqual(self.array.get(0), 20)

    def test_is_empty(self):
        self.assertTrue(self.array.is_empty())
        self.array.append(10)
        self.assertFalse(self.array.is_empty())

    def test_size(self):
        self.assertEqual(self.array.size(), 0)
        self.array.append(10)
        self.assertEqual(self.array.size(), 1)


if __name__ == "__main__":
    unittest.main()
