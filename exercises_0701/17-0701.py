"""
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuirem números negativos
"""
import random

size = 10
array = []

while len(array) < size:
    array.append(random.randrange(-10, 11))


print([number for number in array])
print([number * 0 if number < 0 else number for number in array])
