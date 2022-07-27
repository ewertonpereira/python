"""
Ler dois conjuntos de números reais, amazenando-os em vetores e calcular o produto escalar entre eles . Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalaar, 
sendo que o produto escalar é dado por: x1*y1 + x2*y2 +... +zn*yn.
"""
from random import randint

size = 5
_ = 0

a = []
b = []
c = []

while len(b) < size:
    a.append(randint(0, 50))
    b.append(randint(0, 50))


print([number for number in a])
print([number for number in b])

while len(c) < size:
    c.append(a[_]*b[_])
    _+=1


print([number for number in c])
