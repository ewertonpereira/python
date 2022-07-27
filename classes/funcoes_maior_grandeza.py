"""
Funções de maior grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras
funções como resultado ou menos que podemos passar fnções como argumentos para outras funções, 
e até mesmo criar variáveis do tipo de funções nos nossos programas.

# OBS: Na seção de funções, nós usamos isso.

Em Python as funções são cidadãos de primeira classe - First Class Citizen
"""
# Exemplos - Definindo as funções

def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# Nested Functios - Funções aninhadas

"""
Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
ou também Inner Functions(Funções internas).
"""
# Exemplo

from random import choice

def comprimento(pessoa):
    def humor():
        return choice(('E ai!', 'Suma daqui!', 'Gosto muito de você!'))
    return humor() + pessoa


print(comprimento('Ewerton'))
print(comprimento('FDP'))

# Retornando funções de outras funções

def faz_me_rir():
    def rir():
        return choice(('kkkkkk', 'kpfdkfdkfdokfd', 'hahaha'))
    return rir


# Testando

rindo = faz_me_rir()
print(rindo())

# Ineer Functions - Nested Functions podem acessar o escopo de funções mais externas.

def comprimento(pessoa):
    def humor():
        return choice((f'Salve, {pessoa}!', f'Fuck you {pessoa}!', f'{pessoa}, tu é um bosta!'))
    return humor() 


print(comprimento('Ewerton'))
print(comprimento('FDP'))