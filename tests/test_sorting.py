import unittest
from algorithms.sorting import bubble_sort, insertion_sort, merge_sort


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.data = [64, 25, 12, 22, 11]
        self.expected = [11, 12, 22, 25, 64]

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.data.copy()), self.expected)

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.data.copy()), self.expected)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.data.copy()), self.expected)

    def test_empty_array(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(merge_sort([1]), [1])


if __name__ == "__main__":
    unittest.main()
