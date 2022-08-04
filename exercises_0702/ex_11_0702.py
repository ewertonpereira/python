"""
Leia uma matriz de 3x3 elementos. Calcule ao soma dos elementos que estão na diagonal secundária.
"""
from itertools import count
from ex_04_0702 import create_array_matrices, add_numbers_matrix, show_matrix

size_matrix: int = 3
matrix: list[list[int]] = create_array_matrices(size_matrix)
rand_max: int = 50
final_sum: int = 0
counter: int = (len(matrix) - 1)

add_numbers_matrix(matrix, rand_max)
show_matrix(matrix)

for row in range(len(matrix)):
    final_sum += (matrix[row][counter])
    counter -= 1


print(f'\nA soma dos soma dos elementos que estão na diagonal secundária é: {final_sum}')
