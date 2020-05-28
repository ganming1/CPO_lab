import unittest
from hypothesis import given, settings
import hypothesis.strategies as st
from immutable import *

class TestCaseNode(unittest.TestCase):
    # Sets the instructions to be executed before the test begins
    def setUp(self):
        self.node = Node(7)

    # Sets the instructions to execute after the test has started
    def tearDown(self):
        self.node = None
        del self.node


class TestNodeMethods(TestCaseNode):
    def test_init(self):
        # Check all of nodes attributes
        self.assertEqual(self.node.item, 7)
        self.assertEqual(self.node.next, None)

    def test_str(self):
        self.assertEqual(self.node.__str__(), '7')


class TestCaseLinklistIterator(unittest.TestCase):
    # Sets the instructions to be executed before the test begins
    def setUp(self):
        self.node = Node(11)

    # Sets the instructions to execute after the test has started
    def tearDown(self):
        self.node = None
        del self.node


class TestLinklistIteratorMethods(TestCaseLinklistIterator):
    def test_init(self):
        node = Node(11)
        li = LinklistIterator(node)
        # Check LinklistIterator attribute
        self.assertEqual(li.node, node)

    def test_next(self):
        node = Node(20)
        li = LinklistIterator(node)
        self.assertEqual(li.__next__(), node.item)

    def test_iter(self):
        node = Node(0)
        li = LinklistIterator(node)
        self.assertEqual(str(li.__repr__()), str(li))

class MyTestCase(unittest.TestCase):
    def test_size(self):
        t = ImHashTable(11)
        self.assertEqual(t.size, 11)

    def test_itm_size(self):
        ht = ImHashTable()
        ht.list_to_hashTable([1, 2, 4, 5, 10, 20, 45])
        self.assertEqual(ht.itm_size(), 7)

    @given(st.lists(elements=st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        ht = HashTable(10, a)
        self.assertEqual(ht.itm_size(), len(order_list(a)))

    def test_hash(self):
        self.assertEqual(ImHashTable().hash(10), 0)
        self.assertEqual(ImHashTable().hash(15), 5)

    def test_hashTable_to_list(self):
        ht1 = ImHashTable()
        ht1.list_to_hashTable([3, 5, 28, 90, 34])
        self.assertEqual(ht1.hashTable_to_list(), [90, 3, 34, 5, 28])

    # property-based tests
    @given(st.lists(elements=st.integers()))
    def test_to_list(self, a):
        ht = HashTable(10, a)
        self.assertEqual(ht.hashTable_to_list(), order_list(a))

    def test_list_to_hashTable(self):
        lists = [3, 5, 48, 39]
        ht2 = ImHashTable()
        ht2.list_to_hashTable(lists)
        self.assertEqual(ht2.hashTable_to_list(), lists)

    # property-based tests
    @given(st.lists(elements=st.integers()))
    def test_from_list(self, a):
        ht = HashTable(10, a)
        self.assertEqual(ht.hashTable_to_list(), order_list(a))

    def test_insert(self):
        t = ImHashTable(10, [12])
        self.assertEqual(t.insert(2), t)

    def test_delete(self):
        t = ImHashTable(10, [18, 28,58,68, 38])
        self.assertEqual(t.delete(18).hashTable_to_list(), [18, 28,58,68, 38])
        self.assertEqual(t.delete(38).hashTable_to_list(), [18, 28,58,68, 38])
        self.assertEqual(t.delete(58).hashTable_to_list(), [18, 28,58,68, 38])

    def test_mconcat(self):
        t = ImHashTable(10, [1, 3, 5, 10])
        t2 = HashTable(10, [1, 4, 9])
        self.assertEqual(t.mconcat(t2).hashTable_to_list(), [10, 1, 3, 5])

    def test_reduce(self):
        # sum of empty list
        lst = ImHashTable(0)
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)
        # sum of list
        lst = ImHashTable(10 , [1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)
        # size
        test_data = [
            [],
            [1],
            [1, 2]
        ]
        for e in test_data:
            lst = ImHashTable(10, e)
            self.assertEqual(lst.reduce(lambda st, _: st + 1, 0), lst.itm_size())

    def test_map(self):
        lst = ImHashTable(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        lst.map(str)
        self.assertEqual(lst.hashTable_to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_find(self):
        t = ImHashTable()
        t.list_to_hashTable([10, 3, 51])
        self.assertEqual(t.find(10), True)
        self.assertEqual(t.find(5), False)


if __name__ == '__main__':
    unittest.main()
