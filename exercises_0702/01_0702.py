"""
Leia uma matriz  4x4, e escreva quantos valores maiores que 10 ela possui.
"""
import numpy as np
from random import randint

size_column: int = 4
size_row: int = 4
column: list = []
row: list = []
index_a: int = 0
index_b: int = 0

while index_a < size_column:
    column.append(randint(0, 50))
    index_a+=1


while index_b < size_row:
    row.append(randint(0, 50))
    index_b+=1


print(column)
print(row)
print('---------------------------')

A = np.array([column, row])
print(A)

contador: int = 0
for i in A:
    if i >= 10:
        contador+=1


print(contador)