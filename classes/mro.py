"""
MRO - Method Resolution Order

Method Resolution Order, é a ordem de execução dos métodos(quem será executado primeiro).

Em Python, podemos conferir a order de execução dos métodos de três formas:

    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help

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

pinguim = Pinguim('Osvaldinho')
print(pinguim.cumprimentar()) # Method Resolution Order - MRO

# Method Resolution Order - MRO

print(Pinguim.__mro__)
print(Pinguim.mro())
print(help(Pinguim))
