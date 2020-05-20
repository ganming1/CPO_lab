import unittest
from mutable import *


class MyTestCase(unittest.TestCase):
    def test_size(self):
        t = HashTable(11)
        self.assertEqual(t.size, 11)

    def test_itm_size(self):
        ht = HashTable(10, [1, 2, 4, 5, 10, 20, 45])
        self.assertEqual(ht.itm_size(), 7)

    def test_hash(self):
        self.assertEqual(HashTable().hash(10), 0)
        self.assertEqual(HashTable().hash(15), 5)

    def test_hashTable_to_list(self):
        ht1 = HashTable(10, [3, 5, 28, 90, 34])
        self.assertEqual(ht1.hashTable_to_list(), [90, 3, 34, 5, 28])

    def test_list_to_hashTable(self):
        lists = [3, 5, 48, 39]
        ht2 = HashTable()
        ht2.list_to_hashTable(lists)
        self.assertEqual(ht2.hashTable_to_list(), lists)

    def test_insert(self):
        t = HashTable()
        self.assertEqual(t.insert(12).hashTable_to_list(), [12])
        self.assertEqual(t.insert(12).hashTable_to_list(), [12])

    def test_delete(self):
        t = HashTable(10, [18, 28, 58, 68, 38])
        self.assertEqual(t.delete(18).hashTable_to_list(), [28, 58, 68, 38])
        self.assertEqual(t.delete(38).hashTable_to_list(), [28, 58, 68])
        self.assertEqual(t.delete(58).hashTable_to_list(), [28, 68])

    def test_mconcat(self):
        t = HashTable(10, [1, 3, 5, 10])
        t2 = HashTable(10, [1, 4, 9])
        self.assertEqual(t.mconcat(t2).hashTable_to_list(), [10, 1, 3, 4, 5, 9])

    def test_reduce(self):
        # sum of empty list
        lst = HashTable(0)
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)
        # sum of list
        lst = HashTable(10 , [1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)
        # size
        test_data = [
            [],
            [1],
            [1, 2]
        ]
        for e in test_data:
            lst = HashTable(10, e)
            self.assertEqual(lst.reduce(lambda st, _: st + 1, 0), lst.itm_size())

    def test_map(self):
        lst = HashTable(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        lst.map(str)
        self.assertEqual(lst.hashTable_to_list(), ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

    def test_find(self):
        t = HashTable()
        t.list_to_hashTable([10, 3, 51])
        self.assertEqual(t.find(10), True)
        self.assertEqual(t.find(5), False)


if __name__ == '__main__':
    unittest.main()
