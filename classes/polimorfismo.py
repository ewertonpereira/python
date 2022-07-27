"""
Polimorfismo

Quando reimplementamos um método presente na classe pai em classes filhas estamos realizando uma 
sobreescrita de método (Overriding)

O Overrinding é a melhor representação de polimorfismo.
"""
class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse método!')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')


class Rato(Animal):
     
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala pegaram minha água!')
    
# Testando

jarbas = Gato('Jarbas')
jarbas.comer()
jarbas.falar()

dara = Cachorro('Dara')
dara.comer()
dara.falar()

garoa = Rato('Morador da Garoa')
garoa.comer()
garoa.falar()
 