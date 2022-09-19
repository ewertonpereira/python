from ast import Num
from numbers import Number


class Calculator():

    def addition(self, number1, number2):
        if isinstance(number1, Number) and isinstance(number2, Number):
            return number1 + number2
        else:
            raise Exception('Insira somente números.')

            
    def subtraction(self, number1, number2):
        if isinstance(number1, Number) and isinstance(number2, Number):
            return number1 - number2
        else:
            raise Exception('Insira apenas números.')


    def multiplication(self, number1, number2):
        if isinstance(number1, Number) and isinstance(number2, Number):
            return number1 * number2
        else:
            raise Exception('Insira apenas números.')