import unittest
import math
from Project_Sci_Calc import Calculator

Num1 = Calculator(10,20)


class Calculation(unittest.TestCase):

    def test_Addition(self):
        result = Num1.addition()
        self.assertEqual(result, 30)

    def test_Subtraction(self):
        result = Num1.subtraction()
        self.assertEqual(result, -10)
