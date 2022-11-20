from Book import Book
from os import system
from datetime import datetime


def clear():
    return system('cls')


def is_alpha_space(string):
    return all(char.isalpha() or char.isspace() for char in string)


def get_author_book() -> str:
    author: str = input('Digite o autor: ').strip()
    test = author.replace(' ','')
    if not test.isalpha():
       print('Digite apenas letras: ')
       author: str = get_author_book()
    if is_alpha_space(author) != True:
        #print('Digite apenas letras: ')
        #author: str = get_author_book()
        return author.upper()


def get_title_book() -> str:
    title: str = input('Digite o título do livro: ').strip()
    if not title.isdigit():
        print('Digite apenas letras: ')
        title: str = get_author_book()
    return title.upper()


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
    #pass
    print( result := get_author_book())
