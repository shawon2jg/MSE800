import unittest

# Base class
class Calculator:
    def __init__(self):
        self.result = 0

    def reset(self):
        self.result = 0
        return self.result

# Derived class 1 - inherits from Calculator
class BasicMathOperations(Calculator):
    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

# Derived class 2 - inherits from BasicMathOperations
class AdvancedMathOperations(BasicMathOperations):
    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        self.result = x / y
        return self.result

# Unit test class
class TestMultiplyFunction(unittest.TestCase):
    def setUp(self):
        self.calc = AdvancedMathOperations()

    def test_multiply_positive_numbers(self):
        result = self.calc.multiply(4, 5)
        self.assertEqual(result, 20, "Multiplication of 4 and 5 should equal 20")

    def test_multiply_negative_numbers(self):
        result = self.calc.multiply(-2, -3)
        self.assertEqual(result, 6, "Multiplication of -2 and -3 should equal 6")

    def test_multiply_zero(self):
        result = self.calc.multiply(10, 0)
        self.assertEqual(result, 0, "Multiplication with zero should equal 0")

if __name__ == '__main__':
    unittest.main()
