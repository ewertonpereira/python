from Book import Book
from os import system
from datetime import datetime
import re


def clear():
    return system('cls')

# start email
def regex_email(email) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return True if re.fullmatch(regex, email) else False
    

def get_email() -> str:
    email: str = input('Digite seu email: ')
    if not regex_email(email):
        print('Email inválido!')
        email: str = get_email()
    return email
# end email


def strip_midle_space(word: str) -> str:
    new_word: str = ''
    step: str = ''
    for letter in word:
        if letter != step:
            new_word += letter
            step = letter
    return new_word


def get_name() -> str:
    name: str = input('Digite seu nome: ').strip()
    test = name.replace(' ','')
    if not test.isalpha():
       print('Digite apenas letras: ')
       name: str = get_name()
    return strip_midle_space(name).upper()


def get_author_book() -> str:
    author: str = input('Digite o nome do autor: ').strip()
    test = author.replace(' ','')
    if not test.isalpha():
       print('Digite apenas letras: ')
       author: str = get_author_book()
    return strip_midle_space(author).upper()


def get_title_book() -> str:
    title: str = input('Digite o título do livro: ').strip()
    if not isinstance(title, str):
        print('Digite o título corretamente: ')
        title: str = get_author_book()
    return strip_midle_space(title).upper()


def get_year_book() -> int:
    current_year: int = datetime.today().year
    try:
        year: int = int(input('Digite o ano de lançamento do livro: '))
    except ValueError:
        clear()
        print(f'Digite apenas números!')
        year: int = get_year_book()

    if year < 1500 or year > current_year:
        clear()
        print('O ano deve estar entre 1500 e 2022:')
        year: int = get_year_book()
    return year


def get_weight_book() -> float:
    try:
         weight: float = float(input('Digite o peso do livro: '))
    except ValueError:
        clear()
        print('Digite apenas números.')
        weight: float = get_weight_book()

    if weight < 0 or weight > 2:
        clear()
        print('O peso do livro deve ser maior que zero e menor que 2kg')
        weight: float = get_weight_book()
    return weight


def register_book() -> Book:
    clear()
    author: str = get_author_book()
    title: str = get_title_book()
    year: int = get_year_book()
    weight: float = get_weight_book()
    book: Book = Book(author,title, year, weight)
    return book


if __name__ == '__main__':
    pass
