import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calculator.addition(3, 5), 8)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtraction(7, 5), 2)

    def test_multiplication(self):
        self.assertEqual(Calculator.multiplication(6, 7), 42)

    def test_division(self):
        self.assertEqual(Calculator.division(4, 2), 2)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            Calculator.division(9, 0)

if __name__ == '__main__':
    unittest.main()
