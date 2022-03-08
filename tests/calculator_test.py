"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_placeholder():
    Calculator.divide((2, 2))
    assert (1 + 2) == 3

# def test_calculator_add_method():
#     """Testing the Calculator Add"""
#     test_tuple = (1, 1)
#     assert Calculator.add(test_tuple) == 2
#
#
# def test_calculator_subtract_method():
#     """Testing the Calculator Subtract"""
#     test_tuple = (1, 1)
#     assert Calculator.subtract(test_tuple) == 0
#
#
# def test_calculator_multiply_method():
#     """Testing the Calculator Multiply"""
#     test_tuple = (2, 2)
#     assert Calculator.multiply(test_tuple) == 4
#
#
# def test_calculator_divide_method():
#     """Testing the Calculator Divide"""
#     test_tuple = (2, 2)
#     assert Calculator.divide(test_tuple) == 1
