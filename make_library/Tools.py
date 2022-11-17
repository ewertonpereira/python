from Book import Book
from os import system


def clear():
    return system('cls')


def get_author_book() -> str:
    author: str = input('Digite o autor: ')
    if not isinstance(author, str):
        print('Digite apenas letras: ')
        author: str = get_author_book()
    return author


def get_title_book() -> str:
    title: str = input('Digite o título do livro: ')
    if not isinstance(title, str):
        print('Digite apenas letras: ')
        title: str = get_author_book()
    return title


def get_year_book() -> int:
    try:
        year: int = int(input('Digite o ano de lançamento do livro: '))
    except ValueError:
        clear()
        print(f'Digite apenas números!')
        year: int = get_year_book()

    if year < 1500 or year > 2022:
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



def create_book() -> Book:
    author: str = get_author_book()
    title: str = get_title_book()
    year: int = get_year_book()
    weight: float = get_weight_book()
    book: Book = Book(author,title, year, weight)

    return book


if __name__ == '__main__':
    pass
    # print(result := get_weight_book())
