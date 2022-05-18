import unittest
from salary_per_hour import Employee as EmPrHr
from salary_per_Month import Employee as EmPrMnth

em1 = EmPrHr("Vrushali", 49, 2000)

class TestSalaryPerHr(unittest.TestCase):
    def test_perhour(self):
        result = em1.salary()
        self.assertEqual(result, '98000')