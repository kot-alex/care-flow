import unittest
from algorithms.searching import linear_search, binary_search


class TestSearchingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.unsorted_array = [3, 1, 4, 1, 5, 9, 2, 6]
        self.sorted_array = sorted(self.unsorted_array)

    def test_linear_search_found(self):
        result = linear_search(self.unsorted_array, 5)
        self.assertEqual(result, 5)

    def test_linear_search_not_found(self):
        result = linear_search(self.unsorted_array, 10)
        self.assertIsNone(result)

    def test_binary_search_found(self):
        result = binary_search(self.sorted_array, 5)
        self.assertEqual(result, self.sorted_array.index(5))

    def test_binary_search_not_found(self):
        result = binary_search(self.sorted_array, 10)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
