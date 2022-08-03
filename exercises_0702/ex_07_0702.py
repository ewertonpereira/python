"""
Gerar e imprimir uma matriz de tamanho 10x10, onde seus elementos são da forma:
A[i][j] = 2i + 7j - 2 se i < j;
A[i][j] = 3i² - 1 se i = j;
A[i][j] = 4i³ - 5j² se i > j
"""
from ex_04_0702 import  create_array_matrices, show_matrix

size_matrix:int = 10
matrix: list[int] = create_array_matrices(size_matrix)

for row in range(len(matrix)):
    for column in range(len(matrix)):
        if row < column:
            matrix[row].append(((2 * row) + (7 * column)) - 2)
        elif row == column:
            matrix[row].append((3 * (row ** 2)) - 1)
        else:
            matrix[row].append((4 * (row ** 3)) - (5 * (column ** 2)))
        

show_matrix(matrix)
