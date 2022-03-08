# Imports
from calculator.operations import Addition, Subtraction, Multiplication, Division


# Tests
def test_calculator_operations_add():
    """Testing the Calculator"""
    assert Addition.add(1, 1) == 2


def test_calculator_operations_subtract():
    """Testing the Calculator"""
    assert Subtraction.subtract(2, 1) == 1


def test_calculator_operations_multiply():
    """Testing the Calculator"""
    assert Multiplication.multiply(2, 3) == 6


def test_calculator_operations_division():
    """Testing the Calculator"""
    assert Division.divide(6, 3) == 2
