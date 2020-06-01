import unittest
from hypothesis import given, settings
import hypothesis.strategies as st
from mutable import *


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


# the MyTestCase is the hash map's main faction tests, including the class SingnLinklist's append and find.
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
        lst = HashTable(10, [1, 2, 3])
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

    @given(st.lists(elements=st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        ht = HashTable(10, a)
        self.assertEqual(ht.itm_size(), len(order_list(a)))

    @given(st.lists(elements=st.integers()))
    def test_to_list(self, a):
        ht = HashTable(10, a)
        self.assertEqual(ht.hashTable_to_list(), order_list(a))

    @given(st.lists(elements=st.integers()))
    def test_from_list(self, a):
        ht = HashTable(10, a)
        self.assertEqual(ht.hashTable_to_list(), order_list(a))

    @given(a=st.lists(elements=st.integers()), b=st.lists(elements=st.integers()), c=st.lists(elements=st.integers()))
    def test_monoid_associativity(self, a: int, b: int, c: int) -> None:
        # ht1 + (ht2 + ht3)
        ht1 = HashTable(10, a)
        ht2 = HashTable(10, b)
        ht3 = HashTable(10, c)
        temp = ht2.mconcat(ht3)
        test1 = ht1.mconcat(temp)
        # (ht1 + ht2) + ht3
        ht1 = HashTable(10, a)
        ht2 = HashTable(10, b)
        ht3 = HashTable(10, c)
        temp = ht1.mconcat(ht2)
        test2 = temp.mconcat(ht3)
        self.assertEqual(test1.hashTable_to_list(), test2.hashTable_to_list())

    @given(a=st.lists(st.integers()))
    def test_monoid_identity(self, a) -> None:
        ht1 = HashTable(10, a)
        ht2 = HashTable(10, [])
        # test1 = 0 + ht1
        test1 = ht2.mconcat(ht1)
        # test2 = ht1 + 0
        test2 = ht1.mconcat(ht2)
        self.assertEqual(ht1.hashTable_to_list(), test1.hashTable_to_list())
        self.assertEqual(ht1.hashTable_to_list(), test2.hashTable_to_list())

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
