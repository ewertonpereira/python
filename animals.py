"""
1. Dois cachorros(Bob, e Rex) e um gato(Oli) estão em uma linha. Os cachorros se movem de forma igualitária(para frente e para trás). O gato, está se alimentando. O cachorro que chegar no ponto antes, consegue pegar o gato distraído, caso, os dois cachorros cheguem no ponto do gato no mesmo momento, eles começam a brigar, e o gato consegue fugir.

Sua implementação deve ter uma função que recebe 3 números inteiros sempre positivos, e deve retornar uma string com o nome do animal.
"""
from os import system


# clean terminal screen
def clear():
    return system('cls')


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


def hunt(names: list[str], bob_position: int, rex_position: int, oli_position: int) -> str:

    status: bool = False

    if bob_position == rex_position:
        result = names[2]
    elif oli_position < bob_position and oli_position < rex_position and bob_position != rex_position:
        while status != True:
            bob_position -= 1
            rex_position -= 1
            if bob_position == oli_position:
                status = True
                result = names[0]
            elif rex_position == oli_position:
                status = True
                result = names[1]
    elif oli_position > bob_position and oli_position > rex_position and bob_position != rex_position:
        while status != True:
            bob_position += 1
            rex_position += 1
            if bob_position == oli_position:
                status = True
                result = names[0]
            elif rex_position == oli_position:
                status = True
                result = names[1]

    return result


if __name__ == '__main__':
    clear()
    names: list[str] = ['Bob', 'Rex', 'Oli']

    print('=' * 29)
    print(title := 'The hunt'.center(29))
    print('=' * 29)

    bob_position = get_position(names[0])
    rex_position = get_position(names[1])
    oli_position = get_position(names[2])

    print(bob_position)
    print(rex_position)
    print(oli_position)

    result = hunt(names, bob_position, rex_position, oli_position)
    print(result)
