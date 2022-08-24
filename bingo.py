import copy
from random import randint, shuffle
import os


clear = lambda: os.system('cls')

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
                bingo_card[row].append('x')
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
    print('')


# check if the number raffled is on the card
def check_number(bingo_card: list[list], number: int) -> list[list]:
    for row in range(len(bingo_card)):
        for column in range(len(bingo_card)):
            if bingo_card[row][column] == number:
                bingo_card[row][column] = 'x'


def raffle(card: list[list]) -> int:
    for row in range(len(card[0])):
        for column in range(len(card)):
            bingo: list[int] = ['b', 'i', 'n', 'g', 'o']
            shuffle(bingo)

            if bingo[0] == 'b':
                shuffle(card[0])
                if len(card[0]) > 0:
                    print(f'B - {(element := card[0].pop())}\n'.center(29))
                    return element
            elif bingo[0] == 'i':
                shuffle(card[1])
                if len(card[1]) > 0:
                    print(f'I - {(element := card[1].pop())}\n'.center(29))
                    return element
            elif bingo[0] == 'n':
                shuffle(card[2])
                if len(card[2]) > 0:
                    print(f'N - {(element := card[2].pop())}\n'.center(29))
                    return  element
            elif bingo[0] == 'g':
                shuffle(card[3])
                if len(card[3]) > 0:
                    print(f'G - {(element := card[3].pop())}\n'.center(29))
                    return element
            elif bingo[0] == 'o':
                shuffle(card[4])
                if len(card[4]) > 0:
                    print(f'O - {(element := card[4].pop())}\n'.center(29))
                    return element


if __name__ == '__main__': 

    b: list = add_numbers_list(1, 15)
    i: list = add_numbers_list(16, 30)
    n: list = add_numbers_list(31, 45)
    g: list = add_numbers_list(46, 60)
    o: list = add_numbers_list(61, 75)

    bingo: list[list[int]] = [b, i, n, g, o]
    bingo_raffle = copy.deepcopy(bingo)
    bingo_card: list[list[int]] = create_bingo_card(bingo)
    exit_game: bool = False
    show_matrix(bingo_card)

    while not exit_game:
        check_number(bingo_card, number := raffle(bingo_raffle))
        show_matrix(bingo_card)

        answer: str = input('sair? ')
        if answer == 'sim':
            exit_game = True
        else:
            clear()
    

