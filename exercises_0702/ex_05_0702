"""
Leia uma matrix 5x5. leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e,
ao final, escrever a localização (linha e coluna) ou uma mensagem de 'não encontrado'.
"""
# using functions from the previous exercise (ex_04_0702)
from ex_04_0702 import create_array_matrices, add_numbers_matrix, show_matrix

# get only int numbers
def input_int_value():
    number:int = 0
    try:
        number = int(input('\nDigite um número inteiro: '))
    except ValueError:
        print('\nDigite apenas números.')
        number = input_int_value()


    return number

if __name__ == '__main__':

    size_matrix:int = 5
    max_rand: int = 50
    element: bool = False
    matrix: list = create_array_matrices(size_matrix)
    value_x = input_int_value()
  
    add_numbers_matrix(matrix, max_rand)
    show_matrix(matrix)

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == value_x:
                print(f'\nO valor {value_x} foi encontrado no local {[(row + 1), (column + 1)]} da matriz')
                element = True
          

    if not element:
        print(f'\nO valor {value_x} não está contido na matriz.')
