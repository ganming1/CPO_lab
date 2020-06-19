from dispatch import *
import unittest
import numpy
class FactorialTest(unittest.TestCase):
    def test_Foo_int(self):
        m = Foo()
        self.assertEqual(m.add(1, 2), 3)
        self.assertEqual(m.add(1, 2.1), 3.1)
        self.assertEqual(m.add('1', 12), '112')
        self.assertEqual(m.add(a=1, b=2), 3)
        self.assertEqual(m.add(a='1', b=2), '12')
        self.assertEqual(m.add(a=1, b='2'), '12')
        self.assertEqual(m.add('3', a=1, b=2), '312')
        self.assertEqual(m.add( a=2, b=1), 3)
    def test_Foo_folat(self):
        m = Foo()
        self.assertEqual(m.add(1, 2.1), 3.1)
        self.assertEqual(m.add('1', 12.0), '112.0')
        self.assertEqual(m.add(a=1, b=2.0), 3.0)
        self.assertEqual(m.add(a='1.0', b=2), '1.02')
        self.assertEqual(m.add('3', a=1.0, b=2), '31.02')
    def test_Foo_str(self):
        m = Foo()
        self.assertEqual(m.add('1', 12.0), '112.0')
        self.assertEqual(m.add('1', 12), '112')
        self.assertEqual(m.add(a='1', b=2), '12')
        self.assertEqual(m.add(a=1, b='23'), '123')
        self.assertEqual(m.add('3', a=1, b=2), '312')
        self.assertEqual(m.add( b='1', a=2), '21')
        self.assertEqual(m.add(a='1.0', b=2), '1.02')
        self.assertEqual(m.add('3', a=1.0, b=2), '31.02')
        self.assertEqual(m.Str_Mult('te1',3),'te1te1te1')
    def test_Foo2_Matrix(self):
        m = Foo()
        
        A = np.array([
        [1+1, 1+2, 1+3, 1+4],
        [2+1, 2+2, 2+3, 2+4],
        [3+1, 3+2, 3+3, 3+4]
        ])
        B = np.array([
        [1+1, 1+2, 1+3, 1+4],
        [2+1, 2+2, 2+3, 2+4],
        [3+1, 3+2, 3+3, 3+4]
        ])
        c=np.array([[1,1,1],[2,2,2],[3,3,3],[4,4,4]])
        numpy.testing.assert_array_equal(m.add(A,B),np.array( [[4,6, 8, 10],
        [6, 8, 10, 12],
        [8, 10, 12, 14]]))
        numpy.testing.assert_array_equal(m.MAtrixIntMult(A,3),np.array( [[6,9, 12, 15],
         [9, 12, 15, 18],
         [12, 15, 18, 21]]))
        numpy.testing.assert_array_equal(m.MatrixMult(A,c),np.array([[40,40,40],[50,50,50],[60,60,60]]))
  

    def test_Foo1(self):
        m1 = Foo1()
        self.assertEqual(m1.add(3, 2), 5)
        self.assertEqual(m1.add(1, 11.2), 12.2)
        self.assertEqual(m1.add('s', 12), 's12')
        self.assertEqual(m1.add(a=10, b=2), 12)
        self.assertEqual(m1.add(a='s', b=2), 's2')
        self.assertEqual(m1.add(a=1, b='s'), '1s')
        self.assertEqual(m1.add('3', a=1, b=2), '312')
        A = np.array([
        [1+1, 1+2, 1+3, 1+4],
        [2+1, 2+2, 2+3, 2+4],
        [3+1, 3+2, 3+3, 3+4]
        ])
        B = np.array([
        [1+1, 1+2, 1+3, 1+4],
        [2+1, 2+2, 2+3, 2+4],
        [3+1, 3+2, 3+3, 3+4]
        ])
        c=np.array([[1,1,1],[2,2,2],[3,3,3],[4,4,4]])
        numpy.testing.assert_array_equal(m1.add(A,B),np.array( [[4,6, 8, 10],
        [6, 8, 10, 12],
        [8, 10, 12, 14]]))
        numpy.testing.assert_array_equal(m1.MAtrixIntMult(A,3),np.array( [[6,9, 12, 15],
         [9, 12, 15, 18],
         [12, 15, 18, 21]]))
        numpy.testing.assert_array_equal(m1.MatrixMult(A,c),np.array([[40,40,40],[50,50,50],[60,60,60]]))
    def test_Foo2(self):
        m2 = Foo2()
        self.assertEqual(m2.add(3, 2), 5)
        self.assertEqual(m2.add(1, 11.2), 12.2)
        self.assertEqual(m2.add('s', 12), 's12')
        self.assertEqual(m2.add(a=20, b=2), 22)
        self.assertEqual(m2.add(a='ss', b=2), 'ss2')
        self.assertEqual(m2.add(a=1, b='m'), '1m')
        self.assertEqual(m2.add('s', a=1, b=2), 's12')
        A = np.array([
        [1+1, 1+2, 1+3, 1+4],
        [2+1, 2+2, 2+3, 2+4],
        [3+1, 3+2, 3+3, 3+4]
        ])
        B = np.array([
        [1+1, 1+2, 1+3, 1+4],
        [2+1, 2+2, 2+3, 2+4],
        [3+1, 3+2, 3+3, 3+4]
        ])
        c=np.array([[1,1,1],[2,2,2],[3,3,3],[4,4,4]])
        numpy.testing.assert_array_equal(m2.add(A,B),np.array( [[4,6, 8, 10],
        [6, 8, 10, 12],
        [8, 10, 12, 14]]))
        numpy.testing.assert_array_equal(m2.MAtrixIntMult(A,3),np.array( [[6,9, 12, 15],
         [9, 12, 15, 18],
         [12, 15, 18, 21]]))
        numpy.testing.assert_array_equal(m2.MatrixMult(A,c),np.array([[40,40,40],[50,50,50],[60,60,60]]))

if __name__ == '__main__':
    unittest.main()
