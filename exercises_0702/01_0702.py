"""
Leia uma matriz  4x4, e escreva quantos valores maiores que 10 ele possui.
"""
from random import randint

range_size: int = 4
randon_size: int = 30
matrix: list = [[],[], [], []]

for l in range(0, range_size):
    for c in range(0, range_size):
        matrix[l].append(randint(0, randon_size))
        matrix[c].append(randint(0, randon_size))


print('=-' * 30)

for l in range(0,range_size):
    for c in range(0, range_size):
        print(f'[{matrix[l][c]:^6}]', end = '') 
        # :^6 -> Nº define o número de casas decimais e ^ define como centralizado
    print()

counter:int = 0 

for l in range(0, range_size):
    for c in range(0, range_size):
        if matrix[l][c] > 10:
            counter+=1


print(counter)
