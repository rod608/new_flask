""" This is the Calculator Class """
from calculator.calculations import Addition, Subtraction, Multiplication, Division;


class Calculator:
    """ This is the default result property """

    @staticmethod
    def add(tuple_list):
        """ This is the add method """
        calculation = Addition.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def subtract(tuple_list):
        """ This is the subtract method """
        calculation = Subtraction.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def multiply(tuple_list):
        """ This is the multiply method """
        calculation = Multiplication.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def division(tuple_list):
        """ This is the divide method """
        calculation = Division.create(tuple_list)
        return calculation.get_result()