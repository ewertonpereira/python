class Calculator():
    def sum(self, number1, number2):
        if isinstance(number1, int) and isinstance(number2, int):
            return number1 + number2
        else:
            raise Exception('Insira somente números.')
            