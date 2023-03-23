import string
from os import system

alphabet = list(string.ascii_letters)


def clear():
    return system('cls')


def get_jump() -> int:
    clear()
    number: int = int(input('Digite o número de saltos para criptografia: \n'))
    return number


def get_sentence() -> list[str]:
    clear()
    sentence:list[str] = list(input('Digite sua sentença: \n'))
    return sentence


def question() -> None:
    clear()
    question: str = input(
        'Que tipo de operação você deseja fazer?\n\n0 - Criptografar\n1 - Descriptografar\nQualquer tecla restante para sair\n\n-> ')

    if question == '0':
        print(''.join(list(map(encode, get_sentence()))))  # type: ignore
    elif question == '1':
        print(''.join(list(map(decode, get_sentence()))))  # type: ignore
    else:
        exit()


jump: int = get_jump()

def encode(element: str):
    for letter in range(len(alphabet)):
        if alphabet[letter] == element:
            if element.isupper():
                return alphabet[(letter + jump) % len(alphabet)].upper()
            else: 
                return alphabet[(letter + jump) % len(alphabet)].lower()
        elif element not in alphabet:
            return element


def decode(element: str):
    for letter in range(len(alphabet)):
        if alphabet[letter] == element:
            if element.isupper():
                return alphabet[(letter - jump) % len(alphabet)].upper()
            else: 
                return alphabet[(letter - jump) % len(alphabet)].lower()
        elif element not in alphabet:
            return element


if __name__ == '__main__':
    question()
