"""
Funções com retorno

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None.

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return.

OBS: Não precisamos necessáriamente criar uma variável para receber o retorno de uma função, podemos 
passar a execução da função para outras funções.

# Sobre a palavra reserva return
    - Ela finaliza a função, ou seja, ela sai da execução da função;
    - Podemos ter em uma função, diferentes returns;
    - Podemos em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;

# Exemplo 1

def diz_oi():
    return 'Oi'
    print('Depois do return') # Não vai ser execcutado, pois está depois do return

# Exemplo 2

def new_function():
    variable = False
    if variable:
        return 4
    elif variable is None:
        return 3.2
    return 'b'


print(new_function())

print(diz_oi())

# Exemplo 3

def outra():
    return 2, 3, 4, 5

n1, n2, n3, n4 = outra()
print(n1)
print(n2)
print(n3)
print(n4)

# Vamos criar uma função para jogar uma moeda

from random import random

def joga_meoda():
    # Gera uma número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_meoda())

# Erros comuns na utilização do retorno, que na verdade não é erro, mas sim codificação desnecessária.

def impar():
    num = 6
    if num % 2 != 0:
        return True
    return False

print(impar())
"""
# Exemplo função

num = int(input('Digite um número inteiro: '))
 
def square(number):
    return number ** 2


print(square(num))
