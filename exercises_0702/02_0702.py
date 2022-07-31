"""
Declare uma matriz 5x5. Preencha com 1 a diagonal principal e com zeros os demais elementos. Em seguida escreva a matriz.
"""
# create a matrix of matrices
def create_array_matrices(size_matrix):
    matrix:list = []
    index: int = 0

    while index < size_matrix:
        matrix.append([])
        index+=1


    return matrix

matrix_size: int = 5
matrix: list = create_array_matrices(matrix_size)
index:int = 0

for row in range(0, matrix_size):
    for column in range(0, matrix_size):
        if row == index:
            matrix[row].append(1)
            index+=1
        else:
            matrix[row].append(0)
            matrix[column].append(0)


for row in range(0, matrix_size):
    for column in range(0, matrix_size):
        print(f'[{matrix[row][column]:^5}]', end='')
    print()
