"""
Leia duas matrizes e escreva uma terceira com os valores de cada posição das matrizes lidas.
"""
from ex_04_0702 import create_array_matrices, add_numbers_matrix, show_matrix

size_matrix: int = 4
max_rand: int = 100
matrix_a: list[list] = create_array_matrices(size_matrix)
matrix_b: list[list] = create_array_matrices(size_matrix)
matrix_c: list[list] = create_array_matrices(size_matrix)

add_numbers_matrix(matrix_a, max_rand)
add_numbers_matrix(matrix_b, max_rand)

print('=-=' * 8)
show_matrix(matrix_a)
print('=-=' * 8)
show_matrix(matrix_b)
print('=-=' * 8)

for row in range(len(matrix_c)):
    for column in range(len(matrix_c)):
        if matrix_a[row][column] > matrix_b[row][column]:
            matrix_c[row].append(matrix_a[row][column])
        else:
            matrix_c[row].append(matrix_b[row][column])


show_matrix(matrix_c)
print('=-=' * 8)
