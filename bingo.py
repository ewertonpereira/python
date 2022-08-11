from random import randint, shuffle

# emojis
# https://unicode.org/emoji/charts/full-emoji-list.html

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

# 
def create_bingo_card(matrix: list) -> list[list[int]]:

    matrix_size:int = 5
    bingo_card: list[list[int]] = create_array_matrices(matrix_size)
    
    for row in range(len(bingo_card)):
        for column in range(len(bingo_card)):
            if row == 2 and column == 2:
                bingo_card[row].append('\U0001F505')
            elif column == 0:
                shuffle(matrix[0])
                bingo_card[row].append(element := matrix[0].pop())
            elif column == 1:
                shuffle(matrix[1])
                bingo_card[row].append(element := matrix[1].pop())
            elif column == 2:
                shuffle(matrix[2])
                bingo_card[row].append(element := matrix[2].pop())
            elif column == 3:
                shuffle(matrix[3])
                bingo_card[row].append(element := matrix[3].pop())
            elif column == 4:
                shuffle(matrix[4])
                bingo_card[row].append(element := matrix[4].pop())
                

    return bingo_card


# Shows bingo's matrix values
def show_matrix(matrix: list) -> None:
    print('=' * 29)
    print(title := 'BINGO'.center(29))
    print('=' * 29)
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            print(f'{matrix[row][column]:^6}', end='')
        print('')


    print('=' * 29)


if __name__ == '__main__': 

    b: list = add_numbers_list(1, 15)
    i: list = add_numbers_list(16, 30)
    n: list = add_numbers_list(31, 45)
    g: list = add_numbers_list(46, 60)
    o: list = add_numbers_list(61, 75)

    bingo: list[list[int]] = [b, i, n, g, o]
    bingo_card: list[list[int]] = create_bingo_card(bingo)

    show_matrix(bingo_card)

    