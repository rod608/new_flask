# imports
from calculator.operations import Addition as Add, Subtraction as Subtract, Multiplication as Multiply, Division as Divide


class Calculation:
    """ Calculation abstract base class """

    def __init__(self, tuple_list: tuple):
        """ constructor """
        self.values = Calculation.convert_args_to_tuple_of_float(tuple_list)

    @classmethod
    def create(cls, tuple_list: tuple):
        """ factory method """
        return cls(tuple_list)

    @staticmethod
    def convert_args_to_tuple_of_float(tuple_list):
        """ standardize values to lists of floats"""
        list_values_float = []
        for item in tuple_list:
            list_values_float.append(float(item))
        return tuple(list_values_float)


class Addition(Calculation):
    """ Addition Class - Child of Calculation"""
    @classmethod
    def get_result(self):
        sum_of_values = 0
        for value in self.values:
            sum_of_values = Add.add(value, sum_of_values)
        return sum_of_values

class Subtraction(Calculation):
    """ Subtraction Class - Child of Calculation"""
    @classmethod
    def get_result(self):
        sub_of_values = 0
        for value in self.values:
            sub_of_values = Subtract.subtract(value, sub_of_values)
        return sub_of_values

class Multiplication(Calculation):
    """ Multiplication Class - Child of Calculation"""
    @classmethod
    def get_result(self):
        result_of_values = 1
        for value in self.values:
            result_of_values = Multiply.multiply(value, result_of_values)
        return result_of_values

class Division(Calculation):
    """ Division Class - Child of Calculation"""
    @classmethod
    def get_result(self):
        quotient_of_values = 1
        for value in self.values:
            quotient_of_values = Divide.divide(value, quotient_of_values)
        return quotient_of_values