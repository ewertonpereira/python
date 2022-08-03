"""
Leia uma matriz de 3x3 elementos. Calcule ao soma dos elementos que estão acima da diagonal principal.
"""
from ex_04_0702 import create_array_matrices, add_numbers_matrix, show_matrix

size_matrix: int = 3
matrix: list[list[int]] = create_array_matrices(size_matrix)
rand_max: int = 50
final_sum: int = 0

add_numbers_matrix(matrix, rand_max)
show_matrix(matrix)

for row in range(len(matrix)):
    for column in range(len(matrix)):
        if row == column - 1:
            final_sum+=(matrix[row][column])


print(f'\nA soma dos soma dos elementos que estão acima da diagonal principal é: {final_sum}')
