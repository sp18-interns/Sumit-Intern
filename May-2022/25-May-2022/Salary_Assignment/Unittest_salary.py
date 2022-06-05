import unittest
from Payroll_per_hour import Payroll as EmPrHr
from salary_per_Month import Employee as EmPrMnth

em1 = EmPrHr("Vrushali", 49, 2000, 'manager')
em2 = EmPrHr("Vrushali", 51, 2000, 'Head')


class TestSalaryPerHr(unittest.TestCase):
    def test_Salary_of_e1(self):
        result = em1.salary()
        self.assertEqual(result, 98000)

    def test_Salary_of_e2(self):
        result = em2.salary()
        self.assertEqual(result, 113000.0)

    def test_DA_of_e1(self):
        result = em1.dearness_allowance()
        self.assertEqual(result, 9800)

    def test_Dearness_Allowance_of_e1(self):
        result = em2.dearness_allowance()
        self.assertEqual(result, 10200)

    def test_income_tax_of_e1(self):
        result = em1.income_tax()
        self.assertEqual(result, 10700)

    def test_income_tax_of_e(self):
        result = em2.income_tax()
        self.assertEqual(result, 11300)