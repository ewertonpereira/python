"""
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando os elementos repetidos.
"""
import random

size = 20
goal = 0
array = []

while goal < size:
    array.append(random.randrange(1,30))
    goal += 1

for index, value in enumerate(array):
    print(index, value)


print(set(array))
