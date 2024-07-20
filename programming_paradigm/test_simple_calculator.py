import unittest

import simple_calculator 
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.cal = SimpleCalculator()

    def test_addition(self):
         self.assertEqual(self.calc.add(1, -2), -1, f"test of add(1, -2) was not successful: got {self.cal.add(1, -2)}")

    def test_subtraction(self):
         self.assertEqual(self.calc.subtract(4, 5), -1, f"test of subtract(4, 5) was not successful: got {self.cal.subtract(4, 5)}")

    def test_multiplication(self):
         self.assertEqual(self.calc.multiply(4, 5), 20, f"test of multiply(4, 5) was not successful: got {self.cal.multiply(4, 5)}")

    def test_division(self):
         self.assertEqual(self.calc.divide(self.cal.divide(20, 5), 4, f"test of divide(20, 5) was not successful: got {self.cal.divide(20, 5)}"))
    
    def test_divide_by_zero(self):
        self.assertIsNone(self.cal.divide(20, 0), "Division by zero should return None")

if __name__ == '__main__':
    unittest.main()
