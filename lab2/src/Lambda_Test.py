import unittest

from  Lambda import *


class FactorialTest(unittest.TestCase):
    def test_number(self):
        self.assertEqual(interpret(zero), 0)
        self.assertEqual(interpret(One), 1)
        self.assertEqual(interpret(TWO), 2)
        self.assertEqual(interpret(THREE), 3)
        self.assertEqual(interpret(FIVE), 5)
        self.assertEqual(interpret(SEVEN), 7)

    def test_Increment(self):
        self.assertEqual(interpret(INC(THREE)), 4)
        self.assertEqual(interpret(INC(SIX)),7 )
        self.assertEqual(interpret(INC(FIVE)), 6)

    def test_Addition(self):
        self.assertEqual(interpret(ADD(TWO)(THREE)), 5)
        self.assertEqual(interpret(ADD(TWO)(FOUR)), 6)
        self.assertEqual(interpret(ADD(TWO)(FIVE)), 7)

    def test_Multiplication(self):
        self.assertEqual(interpret(MUL(zero)(THREE)), 0)
        self.assertEqual(interpret(MUL(TWO)(THREE)), 6)
        self.assertEqual(interpret(MUL(FIVE)(FIVE)), 25)

    def test_Decrement(self):
        self.assertEqual(interpret(PRED(FIVE)), 4)
        self.assertEqual(interpret(PRED(TWO)),1)

    def test_TrueorFalse(self):
        self.assertEqual(predicate(C_True), True)
        self.assertEqual(predicate(C_False), False)
        self.assertEqual(predicate(zero), False)
        self.assertEqual(predicate(TWO), True)
    def test_And(self):
        self.assertEqual(predicate(AND(C_False)(C_True)), False)
        self.assertEqual(predicate(AND(C_True)(C_True)), True)

    def test_Or(self):
        self.assertEqual(predicate(OR(C_True)(C_False)), True)
        self.assertEqual(predicate(OR(C_True)(C_True)), True)
        self.assertEqual(predicate(OR(C_False)(C_False)), False)

    def test_Not(self):
        self.assertEqual(predicate(NOT(C_True)), False)
        self.assertEqual(predicate(NOT(C_False)), True)
    
    def test_Pow(self):
        self.assertEqual(interpret(POW(FIVE)(TWO)), 25)
        self.assertEqual(interpret(POW(TWO)(THREE)), 8)

  

    def test_Factorial(self):
        self.assertEqual(interpret(FACT(FIVE)), 120)
        self.assertEqual(interpret(FACT(SIX)), 720)
        


if __name__ == '__main__':
    unittest.main()
