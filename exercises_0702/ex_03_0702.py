"""
Faça um programa que preenche uma matriz 4x4 com o produto do valor da linha e da coluna de cada elemento. Em seguida, imprima na tela a matriz.
"""
def create_array_matrices(matrix_size: int) -> list[list]:
    matrix: list = []
    index:int = 0

    while index < matrix_size:
        matrix.append([])
        index+=1

    
    return matrix

matrix_size:int = 4
matrix: list = create_array_matrices(matrix_size)

for row in range(0, matrix_size):
    for column in range(0, matrix_size):
        matrix[row].append((row + 1) * (column + 1))


for row in range(0, matrix_size):
    for column in range(0, matrix_size):
        print(f'[{matrix[row][column]:^6}]', end='')
    print()

