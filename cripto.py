"""
2. Criptografia de mensagem. Essa cifra, consiste em girar as letras a partir de um seguinte número de posições. Sendo assim, a pessoa que recebe a mensagem, sabe quantas posições voltar, e portanto, terá a mensagem original. Sua tarefa é, dado um texto qualquer, realizar a rotação.

Obs: Não precisa considerar caracteres com acentos, como: á, à e etc…
"""
from os import system
import string


# clean terminal screen
def clear():
    return system('cls')


# sets the number for encryption
def rotation_number() -> int:
    try:
        rotation: int = int(input('Informe o número de rotações: '))
    except ValueError:
        clear()
        print('Digite apenas números inteiros')
        rotation: int = rotation_number()

    return rotation


def start() -> None:
    clear()
    rotation: int = rotation_number()
    clear()
    text: str = input('Digite seu texto: ').lower()
    print(text)
    
    alphabet: list[str] = list(string.ascii_lowercase)
    size: int = len(alphabet)

    new_text: str = ''
    for letter in text:
        if letter == ' ' or letter == '!' or letter == '?' or letter == ',' or letter == '.':
            new_text += letter
        elif letter in alphabet:
            index = alphabet.index(letter)
            new_letter = alphabet[(index + rotation) % size]
            new_text += new_letter

    clear()
    print(f'{text}\n')
    print(f'\n{new_text}')


if __name__ == '__main__':
    start()