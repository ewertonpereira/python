"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Esse processo é chamado de serialização/deserialização

OBS: O módulo Pickle não é seguro contra dados maliciosos e  dessa forma não é recomendado trabalhar
com arquivos Pickle vindos de outras pessoas que você não conheça ou de fontes desconhecidas.


"""
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendoo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
         print(f'{self.nome} está latindo...')



# Fazendo a escrita em arquivos Pickle

jarbas = Gato('Jasbas')
dara = Cachorro('Dara')

with open('animais.pickle', 'wb') as file:
    pickle.dump((jarbas, dara), file)


# Fazer a leitura de dados em arquivos Pickle

with open('animais.pickle', 'rb') as file:
    gato, cachorro = pickle.load(file)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachrro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do gato é {type(cachorro)}')

