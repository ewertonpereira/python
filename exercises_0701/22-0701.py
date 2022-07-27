"""
Faça um program que leia dois vetores de 10 posições e calcule outro vetor contendo nas posições pares os valores do primeiro e nas posições impares os valores do segundo.
"""
import random

size = 10
_ = 0

a = []
b = []
c = []


while len(b) < size:
    a.append(random.randrange(0, 50))
    b.append(random.randrange(0, 50))
    

print([number for number in a])
print([number for number in b])

while len(c) < (len(a)+len(b)):
    c.append(a[_])
    c.append(b[_])
    _+=1


print([number for number in c])
