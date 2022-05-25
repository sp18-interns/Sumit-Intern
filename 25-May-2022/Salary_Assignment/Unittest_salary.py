import unittest
from salary_per_hour import Payroll as EmPrHr
from salary_per_Month import Employee as EmPrMnth

em1 = EmPrHr("Vrushali", 49, 2000)
em2 = EmPrHr("Vrushali", 51, 2000)


class TestSalaryPerHr(unittest.TestCase):
    def test_per_hour01_Salary(self):
        result = em1.salary()
        self.assertEqual(result, 98000)

    def test_per_hour02_Salary(self):
        result = em2.salary()
        self.assertEqual(result, 113000.0)

    def test_per_hour03_DA(self):
        result = em1.dearness_allowance()
        self.assertEqual(result, 9800)

    def test_per_hour04_DA(self):
        result = em2.dearness_allowance()
        self.assertEqual(result, 10200)

    def test_per_hour05_IT(self):
        result = em1.income_tax()
        self.assertEqual(result, 10700)

    def test_per_hour06_IT(self):
        result = em2.income_tax()
        self.assertEqual(result, 11300)