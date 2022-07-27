"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os dois vetores anteriores, ou, seja 
que tem apenas os números que estão nos dois vetores. Não deve conter números repetidos.
"""
from random import randint

array1 = []
array2 = []
array3 = []
size = 10

while len(array2) < size:
    array1.append(randint(0, 10))
    array2.append(randint(0, 10))


print([num for num in array2])
print([num for num in array1])

array3 = set(array1).intersection(set(array2))

print(list(num for num in array3))
