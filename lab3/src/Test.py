from dispatch import *
import unittest

class FactorialTest(unittest.TestCase):
    def test_Foo(self):
        a = Foo()
        self.assertEqual(a.add(1,2),3)
        self.assertEqual(a.add(1,2.1),3.1)
        self.assertEqual(a.add('1',12),'112')
        self.assertEqual(a.add(n=1,m=2),3)
        self.assertEqual(a.add(n='1',m=2),'12')
        self.assertEqual(a.add(n=1,m='2'),'12')
        self.assertEqual(a.add('3',n=1,m=2),'312')
    def test_Foo1(self):
        b = Foo1()
        self.assertEqual(b.add(3,2),5)
        self.assertEqual(b.add(1,11.2),12.2)
        self.assertEqual(b.add('s',12),'s12')
        self.assertEqual(b.add(n=10,m=2),12)
        self.assertEqual(b.add(n='s',m=2),'s2')
        self.assertEqual(b.add(n=1,m='s'),'1s')
        self.assertEqual(b.add('3',n=1,m=2),'312')
    def test_Foo2(self):
        b = Foo2()
        self.assertEqual(b.add(3,2),5)
        self.assertEqual(b.add(1,11.2),12.2)
        self.assertEqual(b.add('s',12),'s12')
        self.assertEqual(b.add(n=20,m=2),22)
        self.assertEqual(b.add(n='ss',m=2),'ss2')
        self.assertEqual(b.add(n=1,m='m'),'1m')
        self.assertEqual(b.add('s',n=1,m=2),'s12')
if __name__ == '__main__':
    unittest.main()