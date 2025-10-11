import doctest
import math

"""
This is the "example" module.
The example module supplies one function, factorial().  For example,
>>> factorial(5)
120
"""

def factorial(n):
    """
    The code includes:
        (a) A docstring at the module level explaining the module and its main function, factorial.
        (b) A factorial function that returns the factorial of a non-negative number.
        (c) Docstring tests via the doctest module to verify the behavior of the function.
        (d) A main block that executes the doctests when executed as a script.

    The module doctest is utilized to execute the test cases in the docstrings, comparing the code's output with the desired output.

    Return the factorial of n, an exact integer >= 0
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    >>> factorial(34)
    295232799039604140847618609643520000000

    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")

    result = 1
    factor = 2

    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == "__main__":
    doctest.testmod()
