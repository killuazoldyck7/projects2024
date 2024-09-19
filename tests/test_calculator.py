"""
Test module for the calculator functions.
"""

from calculator import add, subtract

def test_addition():
    """
    Test the addition of two numbers using the add function.

    This test checks that the add function returns the correct sum
    when given the numbers 2 and 2.
    """
    assert add(2, 2) == 4

def test_subtract():
    """
    Test the subtraction of two numbers using the subtract function.

    This test checks that the subtract function returns the correct value
    when given the numbers 2 and 2.
    """
    assert subtract(2, 2) == 0
