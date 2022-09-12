"""
1. Dois cachorros(Bob, e Rex) e um gato(Oli) estão em uma linha. Os cachorros se movem de forma igualitária(para frente e para trás). O gato, está se alimentando. O cachorro que chegar no ponto antes, consegue pegar o gato distraído, caso, os dois cachorros cheguem no ponto do gato no mesmo momento, eles começam a brigar, e o gato consegue fugir.

Sua implementação deve ter uma função que recebe 3 números inteiros sempre positivos, e deve retornar uma string com o nome do animal.
"""
from os import system


# clean terminal screen
def clear():
    return system('cls')


# shows the position of each animal
def get_position(name: str) -> int:
    try:
        position: int = int(input(f'\nDigite a posição inicial do {name}: '))
        if position < 0:
            clear()
            print('Digite apenas números positivos.\n')
            position = get_position(name)
        elif type(position) != int:
            clear()
            print('Digite apenas números inteiros.\n')
            position = get_position(name)
    except ValueError:
        clear()
        print('Digite apenas números.\n')
        position = get_position(name)

    return position


# show who wins the hunt
def hunt(names: list[str], bob_position: int, rex_position: int, oli_position: int) -> str:

    status: bool = False

    # if the position of the dogs are the same
    if bob_position == rex_position:
        status = True
        result = f'\n{names[2]}, ele fugiu...'
    # if oli's position is less than both
    elif oli_position < bob_position and oli_position < rex_position and bob_position != rex_position:
        while status != True:
            bob_position -= 1
            rex_position -= 1
            if bob_position == oli_position:
                status = True
                result = f'\n{names[0]}, ele pegou o gato!'
            elif rex_position == oli_position:
                status = True
                result = f'\n{names[1]}, ele pegou o gato!'
    # if oli's position is greater than both
    elif oli_position > bob_position and oli_position > rex_position and bob_position != rex_position:
        while status != True:
            bob_position += 1
            rex_position += 1
            if bob_position == oli_position:
                status = True
                result = f'\n{names[0]}, ele pegou o gato!'
            elif rex_position == oli_position:
                status = True
                result = f'\n{names[1]}, ele pegou o gato!'
    # if oli's position is greater than bob and less than rex
    elif oli_position > bob_position and oli_position < rex_position and bob_position != rex_position:
        while status != True:
            bob_position += 1
            rex_position -= 1
            if bob_position == oli_position:
                status = True
                result = f'\n{names[0]}, ele pegou o gato!'
            elif rex_position == oli_position:
                status = True
                result = f'\n{names[1]}, ele pegou o gato!'
    # if oli's position is less than bob and bigger than rex
    elif oli_position < bob_position and oli_position > rex_position and bob_position != rex_position:
        while status != True:
            bob_position += 1
            rex_position -= 1
            if bob_position == oli_position:
                status = True
                result = f'\n{names[0]}, ele pegou o gato!'
            elif rex_position == oli_position:
                status = True
                result = f'\n{names[1]}, ele pegou o gato!'
    
    return result


def start():
    clear()
    names: list[str] = ['Bob', 'Rex', 'Oli']
    bob_position = get_position(names[0])
    rex_position = get_position(names[1])
    oli_position = get_position(names[2])

    print('=' * 29)
    print(title := 'A CAÇADA'.center(29))
    print('=' * 29)
    clear()
    print('=' * 29)
    print(title := 'O VENCEDOR É...'.center(29))
    print('=' * 29)
    print(result := hunt(names, bob_position, rex_position, oli_position))

if __name__ == '__main__':
    start()
