import unittest
from data_structures.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_insert_and_search(self):
        self.hash_table.insert("key1", "value1")
        self.assertEqual(self.hash_table.search("key1"), "value1")

    def test_update_value(self):
        self.hash_table.insert("key1", "value1")
        self.hash_table.insert("key1", "new_value")
        self.assertEqual(self.hash_table.search("key1"), "new_value")

    def test_delete(self):
        self.hash_table.insert("key1", "value1")
        self.assertTrue(self.hash_table.delete("key1"))
        self.assertIsNone(self.hash_table.search("key1"))

    def test_resize(self):
        for i in range(15):  # Assuming the default size is 10
            self.hash_table.insert(f"key{i}", f"value{i}")
        initial_size = self.hash_table.size
        self.hash_table.resize()
        self.assertGreater(self.hash_table.size, initial_size)


if __name__ == "__main__":
    unittest.main()
