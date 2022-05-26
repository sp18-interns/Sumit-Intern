import unittest
from Payroll_per_hour import Payroll as EmPrHr
from salary_per_Month import Employee as EmPrMnth

em1 = EmPrHr("Vrushali", 49, 2000)
em2 = EmPrHr("Vrushali", 51, 2000)


class TestSalaryPerHr(unittest.TestCase):
    def Salary_of_e1(self):
        result = em1.salary()
        self.assertEqual(result, 98000)

    def Salary_of_e2(self):
        result = em2.salary()
        self.assertEqual(result, 113000.0)

    def DA_of_e1(self):
        result = em1.dearness_allowance()
        self.assertEqual(result, 9800)

    def Dearness_Allowance_of_e1(self):
        result = em2.dearness_allowance()
        self.assertEqual(result, 10200)

    def income_tax_of_e1(self):
        result = em1.income_tax()
        self.assertEqual(result, 10700)

    def income_tax_of_e(self):
        result = em2.income_tax()
        self.assertEqual(result, 11300)