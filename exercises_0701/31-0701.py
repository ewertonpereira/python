"""
Faça um programa que leia dos vetores de 10 elementos. Crie um vetor que seja a união dos dois vetores anteriores, ou seja, que contém os 
números dos dois vetores. Não deve conter números repetidos.
"""
from random import randint

vector1 = []
vector2 = []
vector3 = []
size = 10

while len(vector2) < size:
    vector1.append(randint(0, 10))
    vector2.append(randint(0, 10))


print(list(num for num in vector1))
print(list(num for num in vector2))

vector3 = set(vector1).union(set(vector2))

print([num for num in vector3])
