import unittest

from calculator import Calculator, CalculatorError


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.evaluate("2 + 3"), 5)

    def test_operator_precedence(self):
        self.assertEqual(self.calc.evaluate("2 + 3 * 4"), 14)

    def test_parentheses(self):
        self.assertEqual(self.calc.evaluate("(2 + 3) * 4"), 20)

    def test_exponentiation(self):
        self.assertEqual(self.calc.evaluate("2 ** 3"), 8)

    def test_negative_numbers(self):
        self.assertEqual(self.calc.evaluate("-7 + 2"), -5)

    def test_division_by_zero(self):
        with self.assertRaises(CalculatorError):
            self.calc.evaluate("10 / 0")


if __name__ == "__main__":
    unittest.main()
