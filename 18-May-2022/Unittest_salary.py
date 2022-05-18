import unittest
from salary_per_hour import Employee as EmPrHr
from salary_per_Month import Employee as EmPrMnth

em1 = EmPrHr("Vrushali", 49, 2000)
em2 = EmPrHr("Vrushali", 51, 2000)


class TestSalaryPerHr(unittest.TestCase):
    def test_perhour(self):
        result = em1.salary()
        self.assertEqual(result, '98000')

    def test_perhour1(self):
        result = em2.salary()
        self.assertEqual(result, 'OT113000.0')
