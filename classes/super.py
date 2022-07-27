"""
O método super()

O método super() se refere à super classe.
"""
class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O  {self.__nome} fala {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        Animal.__init__(self, nome, especie)
        #super().__init__(nome, especie) # Recomendado
        self.__raca = raca


jarbas = Gato('Jarbas', 'Felino', 'RND')
jarbas.faz_som('miau')
