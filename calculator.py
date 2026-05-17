"""Simple calculator module."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the division of a by b."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def power(a, b):
    """Return a raised to the power of b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numeric.")
    return a ** b