"""
Faça um programa para gerar automáticamente números entre 0 e 99 de uma cartela de bingo. Sabendo que cada cartela deverá conter 5 linhas de 5 núneros, gere estes dados de modo a não
ter números repetidos dentro das cartelas. O programa deve exibir na tela a cartela gerada.
"""
from random import randint, shuffle

# create a matrix with non-repeating numbers
def matrix_not_repeated_numbers(row_size: int, column_size: int, min_rand: int, max_rand: int) -> list[list[int]]:
    
    matrix_size: int = (row_size * column_size)
    list_numbers: list[int]= []
    matrix: list[list] = []
    index: int = 0
    counter: int = 0

    while index < row_size:
        matrix.append([])
        index += 1

    # uses set to don't repeat numbers
    while len(list_numbers) < matrix_size:
        list_numbers.append(randint(min_rand, max_rand))
        list_numbers = (set(list_numbers))
        list_numbers = (list(list_numbers))
        shuffle(list_numbers)
        

    for row in range(row_size):
        for column in range(column_size):
            matrix[row].append(list_numbers[counter])
            counter += 1 
    
    
    return matrix


if __name__ == '__main__':
    from ex_04_0702 import show_matrix

    row_size: int = 5 
    column_size: int = 5 
    min_rand: int = 0
    max_rand: int = 99
    matrix: list[list[int]] = matrix_not_repeated_numbers(row_size, column_size, min_rand, max_rand)
  
    print('=' * 29)
    print(title := 'BINGO'.center(29))
    print('=' * 29)
    show_matrix(matrix)
    print('=' * 29)
