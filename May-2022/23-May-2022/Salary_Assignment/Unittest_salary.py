import unittest
from salary_per_hour import Employee as EmPrHr
from salary_per_Month import Employee as EmPrMnth

em1 = EmPrHr("Vrushali", 49, 2000)
em2 = EmPrHr("Vrushali", 51, 2000)


class TestSalaryPerHr(unittest.TestCase):
    def test_perhour01_Salary(self):
        result = em1.salary()
        self.assertEqual(result, 98000)

    def test_perhour02_Salary(self):
        result = em2.salary()
        self.assertEqual(result, 113000.0)

    def test_perhour03_DA(self):
        result = em1.deerness_allowance()
        self.assertEqual(result, 9800)

    def test_perhour04_DA(self):
        result = em2.deerness_allowance()
        self.assertEqual(result, 10200)

    def test_perhour05_IT(self):
        result = em1.income_tax()
        self.assertEqual(result, 10700)

    def test_perhour06_IT(self):
        result = em2.income_tax()
        self.assertEqual(result, 11300)
