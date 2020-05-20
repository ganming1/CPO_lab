import unittest

from visualized import *

class FactorialTest(unittest.TestCase):
    def test_Factorial(self):
        self.assertEqual(interpret(FACT(SIX)), 720)

   

    

if __name__ == '__main__':
    unittest.main()
