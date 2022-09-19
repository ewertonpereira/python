from numbers import Number


class Calculator():

    def addition(self, number1: Number, number2: Number) -> Number:
        if isinstance(number1, Number) and isinstance(number2, Number):
            return number1 + number2
        else:
            raise Exception('Insira somente números.')

            
    def subtraction(self, number1: Number, number2: Number) -> Number:
        if isinstance(number1, Number) and isinstance(number2, Number):
            return number1 - number2
        else:
            raise Exception('Insira apenas números.')


    def multiplication(self, number1: Number, number2: Number) -> Number:
        if isinstance(number1, Number) and isinstance(number2, Number):
            return number1 * number2
        else:
            raise Exception('Insira apenas números.')


    def division(self, number1: Number, number2: Number) -> Number:
        if isinstance(number1, Number) and isinstance(number2, Number) and number2 != 0:
            return number1 / number2
        else:
            raise Exception('Insira apenas números.')

