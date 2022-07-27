"""
Escrevendo um iterador customizado
"""
class Contador:
    def __init__(self, menor, maior) :
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self


    def __next__(self):
        if self.menor < self.maior:
            number = self.menor
            self.menor = self.menor + 1
            return number
        raise StopIteration


for number in Contador(1, 11):
    print(number)

