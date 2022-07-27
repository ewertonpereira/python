"""
Herança Múltipla

Herança múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, 
fazendo que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herença múltipla pode ser feita de duas maneiras: 

    - Por multiderivação direta
    - Por multiderivação indireta

# Exemplo 1 - Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class MultiDerivada(Base1, Base2):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class MultiDerivada(Base2):
    pass


OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos 
os atributos e métodos das super classes.
"""
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terreste(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Aquatico, Terreste):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terreste('Chico')
print(tatu.andar())
print(tatu.cumprimentar())

pinguim = Pinguim('Osvaldinho')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar()) # Method Resolution Order - MRO

# Objeto é instância de...

print(f'Osvaldinho é instância de Pinguim? {isinstance(pinguim, Pinguim)}')
print(f'Osvaldinho é instância de Aquatico? {isinstance(pinguim, Aquatico)}')
print(f'Osvaldinho é instância de Terrestre? {isinstance(pinguim, Terreste)}')
print(f'Osvaldinho é instância de Animal? {isinstance(pinguim, Animal)}')
print(f'Osvaldinho é instância de Object? {isinstance(pinguim, object)}')
