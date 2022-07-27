"""
Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos em suas respectivas posições no vetor.
"""
from random import randint

size = 10
array = []

while len(array) < size:
    array.append(randint(0,50))


print([number for number in array])

print([f'Index: {index}  Valor: {value}' for index, value in enumerate(array) if value % 2])
