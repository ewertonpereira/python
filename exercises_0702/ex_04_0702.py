"""
leia uma matriz 4x4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor.
"""
from random import randint

# create a matrix of matrices
def create_array_matrices(size_matrix: int) -> list[list]:
    matrix: list[list] = []
    index: int = 0
    while index < size_matrix:
        matrix.append([])
        index+=1

    return matrix


# add random integer numbers in the matrix
def add_numbers_matrix(matrix: list) -> list[int]:
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row].append(randint(0,50))


    return matrix


# Shows matrix's values
def show_matrix(matrix: list) -> None:
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            print(f'{matrix[row][column]:^6}', end='')
        print('')


# shows the location of the largest number
def local_number(matrix: list) -> None:
    max: int = 0
    answer_row: int = 0
    answer_column: int = 0

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] > max:
                max = matrix[row][column]
                answer_row = row
                answer_column = column

    return print(f'\nO maior número se encontra na posição {[(answer_row + 1), (answer_column + 1)]}\n')


# data for this file
if __name__ == '__main__':
    size_matrix: int = 4
    matrix: list = create_array_matrices(size_matrix)
    add_numbers_matrix(matrix)
    show_matrix(matrix)
    local_number(matrix)
    