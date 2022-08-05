"""
Gere uma matriz com 4x4 com valores no intervalo [1-20]. Escreva um programa que transforme a matriz gerada numa matriz triangular inferior,
 ou seja, atribuindo zero a todos os elementos acima da diagonal principal. imprima a matriz principal e a matriz tranformada.
"""
from random import randint

def add_matrix_number_min_max(matrix: list, min_range: int, max_range:int) -> list[list[int]]:
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row].append(randint(min_range, max_range))


    return matrix


if __name__ == '__main__':
    from ex_04_0702 import create_array_matrices, show_matrix

    size_matrix: int = 4
    min_range: int = 1
    max_range: int = 20
    matrix: list[list[int]] = create_array_matrices(size_matrix)

    add_matrix_number_min_max(matrix, min_range, max_range)
    show_matrix(matrix)
    print('')

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if row < column:
                matrix[row][column] = 0
            

    show_matrix(matrix)
