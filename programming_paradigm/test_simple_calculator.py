import unittest
import simple_calculator 

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.cal = simple_calculator.SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.cal.add(1, -2), -1, f"test of add(1, -2) was not successful: got {self.cal.add(1, -2)}")

    def test_subtract(self):
        self.assertEqual(self.cal.subtract(4, 5), -1, f"test of subtract(4, 5) was not successful: got {self.cal.subtract(4, 5)}")

    def test_multiply(self):
        self.assertEqual(self.cal.multiply(4, 5), 20, f"test of multiply(4, 5) was not successful: got {self.cal.multiply(4, 5)}")

    def test_divide(self):
        self.assertEqual(self.cal.divide(20, 5), 4, f"test of divide(20, 5) was not successful: got {self.cal.divide(20, 5)}")
    
    def test_divide_by_zero(self):
        self.assertIsNone(self.cal.divide(20, 0), "Division by zero should return None")

if __name__ == '__main__':
    unittest.main()