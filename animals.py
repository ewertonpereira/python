"""
1. Dois cachorros(Bob, e Rex) e um gato(Oli) estão em uma linha. Os cachorros se movem de forma igualitária(para frente e para trás). O gato, está se alimentando. O cachorro que chegar no ponto antes, consegue pegar o gato distraído, caso, os dois cachorros cheguem no ponto do gato no mesmo momento, eles começam a brigar, e o gato consegue fugir.

Sua implementação deve ter uma função que recebe 3 números inteiros sempre positivos, e deve retornar uma string com o nome do animal.
"""
from os import system


# clean terminal screen
def clear(): 
    return system('cls')


def get_name(name:str):
    try:
        position: int = int(input(f'\nDigite a posição inicial do {name}: '))
        if position < 0:
            clear()
            print('Digite apenas números positivos.\n')
            position = get_name(name)
        elif type(position) != int:
            clear()
            print('Digite apenas números inteiros.\n')
            position = get_name(name)
    except ValueError:
        clear()
        print('Digite apenas números.\n')
        position = get_name(name)
        
    return position


if __name__ == '__main__':
    clear()
    bob: str = 'Bob'
    rex: str = 'Rex'
    oli: str = 'Oli'

    print('=' * 29)
    print(title := 'The hunt'.center(29))
    print('=' * 29)

    bob_position = get_name(bob)
    rex_position = get_name(rex)
    oli_position = get_name(oli)

    print(bob_position)
    print(rex_position)
    print(oli_position)
