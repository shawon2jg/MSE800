import doctest

# Base class
class Calculator:
    def __init__(self):
        self.result = 0

    def reset(self):
        """
        Resets the calculator result to 0.
        >>> calc = Calculator()
        >>> calc.reset()
        0
        """
        self.result = 0
        return self.result

# Derived class 1 - inherits from Calculator
class BasicMathOperations(Calculator):
    def add(self, x, y):
        """
        Adds two numbers and stores the result.
        >>> calc = BasicMathOperations()
        >>> calc.add(2, 3)
        5
        """
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        """
        Subtracts y from x and stores the result.
        >>> calc = BasicMathOperations()
        >>> calc.subtract(5, 3)
        2
        """
        self.result = x - y
        return self.result

# Derived class 2 - inherits from BasicMathOperations
class AdvancedMathOperations(BasicMathOperations):
    def multiply(self, x, y):
        """
        Multiplies two numbers and stores the result.
        >>> calc = AdvancedMathOperations()
        >>> calc.multiply(4, 5)
        20
        >>> calc.multiply(-2, -3)
        6
        >>> calc.multiply(10, 0)
        0
        """
        self.result = x * y
        return self.result

    def divide(self, x, y):
        """
        Divides x by y and stores the result.
        >>> calc = AdvancedMathOperations()
        >>> calc.divide(10, 2)
        5.0
        """
        self.result = x / y
        return self.result

    def mod(self, x, y):
        """
        Divides x by y and stores the result.
        >>> calc = AdvancedMathOperations()
        >>> calc.mod(10, 2)
        0
        """
        self.result = x % y
        return self.result

if __name__ == '__main__':
    doctest.testmod()