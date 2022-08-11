from random import randint, shuffle

# create a matrix of matrices
def create_array_matrices(size_matrix: int) -> list[list]:
    matrix: list[list] = []
    index: int = 0
    while index < size_matrix:
        matrix.append([])
        index+=1

    return matrix


"""
adds numbers to the list according to the given range
(e.g.) -> min_rand: 1 | max_rand: 15 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""
def add_numbers_list(min_rand: int, max_rand: int) -> list[int]:
    array:list[int] = []
    while min_rand <= max_rand:
        array.append(min_rand)
        min_rand += 1


    return array


# Shows matrix's values
def show_matrix(matrix: list) -> None:
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            print(f'{matrix[row][column]:^6}', end='')
        print('')


b: list = add_numbers_list(1, 15)
i: list = add_numbers_list(16, 30)
n: list = add_numbers_list(31, 45)
g: list = add_numbers_list(46, 60)
o: list = add_numbers_list(61, 75)

bingox: list[list[int]] = [b, i, n, g, o]

def bingo(matrix: list) -> list[list[int]]:

    matrix_size:int = 5
    bingo_matrix: list[list[int]] = create_array_matrices(matrix_size)
    
    for row in range(len(bingo_matrix)):
        for column in range(len(bingo_matrix)):
            if row == 2 and column == 2:
                bingo_matrix[row].append('x')
            elif column == 0:
                shuffle(matrix[0])
                bingo_matrix[row].append(element := matrix[0].pop())
            elif column == 1:
                shuffle(matrix[1])
                bingo_matrix[row].append(element := matrix[1].pop())
            elif column == 2:
                shuffle(matrix[2])
                bingo_matrix[row].append(element := matrix[2].pop())
            elif column == 3:
                shuffle(matrix[3])
                bingo_matrix[row].append(element := matrix[3].pop())
            elif column == 4:
                shuffle(matrix[4])
                bingo_matrix[row].append(element := matrix[4].pop())


    return bingo_matrix


#print(bingo(bingox))
print(show_matrix(bingo(bingox)))
