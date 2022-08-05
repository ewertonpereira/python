"""
Leia uma matriz de 3x3 elementos. Calcule e imprima sua transposta.
"""
from ex_04_0702 import create_array_matrices, add_numbers_matrix, show_matrix

size_matrix: int = 3
max_rand: int = 50
matrix_a: list[list[int]] = create_array_matrices(size_matrix)
matrix_b: list[list[int]] = create_array_matrices(size_matrix)

add_numbers_matrix(matrix_a, max_rand)
show_matrix(matrix_a)

for row in range(len(matrix_b)):
    for column in range(len(matrix_b)):
        matrix_b[column].append(matrix_a[row][column])


print('')
show_matrix(matrix_b)
