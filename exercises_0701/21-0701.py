"""
Faça um programa que receba do usuário  dois vetores A e B, com 10 elementos inteiros cada. Crie um novo vetor denominado C calculando  C = A - B, mostre os dados do vetor C.
"""
import random

size = 10
goal = 0
a = []
b = []
c = []


while  goal < size:
    a.append(random.randrange(0, 50))
    b.append(random.randrange(0, 50))
    c.append(a[goal] - b[goal])
    goal += 1


print([number for number in a])
print([number for number in b])
print([number for number in c])
