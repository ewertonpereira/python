"""
Leia dois vetores x e y, cada um com 5 elementos. Calcule e mostre os vetores resultantes de cada caso a baixo: 

    - Soma entre x e y, soma cada elemento de x com o da mesma posição em y.
    - Produto entre x e y, multipliaca cada elemento de x com o da mesma posição em y.
    - Diferença entre x e y, todos os elementos de x que não existem em y.
    - Intersecção entre x e y, apenas os elementos que aparecem nos dois vetores.
    - União entre x e y, todos os elementos de x, e todos os elementos de y que não estão em x.
"""
from random import randint

array1 = []
array2 = []
array3 = []
size_array = 5

def mult(number1, number2):
    return number1 * number2

while len(array2) < size_array:
    array1.append(randint(0, 25))
    array2.append(randint(0, 25))
    

print(f'X: {[num for num in array1]}')
print(f'Y: {[num for num in array2]}')

array_sum = map(lambda array_sum: sum(array_sum), zip(array1, array2))
print(f'Lista de somas:\n{list(array_sum)}')

array_multiplication = list(map(lambda x, y: x * y ,array1, array2))
print(f'Lista de multiplicações:\n{list(array_multiplication)}')

print(f'Diferença de x para y:\n{list(set(array1).difference(set(array2)))}')

print(f'Interseção de x para y:\n{list(set(array1).intersection(set(array2)))}')

print(f'união de x para y:\n{list(set(array1).union(set(array2)))}')
