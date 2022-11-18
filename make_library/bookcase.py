import pandas as pd
from Tools import register_book

class Bookcase:

    
    def __init__(self,size, max_weight) -> None:
        self.bookcase = pd.DataFrame(columns=['ID', 'Autor', 'Título', 'Ano', 'Peso'])
        self.size: int = size
        self.max_weight: float = max_weight
        self.weight: float = 0
        

    def add_book(self) -> None:
        self.clear()
        if len(self.bookcase) <= (self.size - 1):
            book = register_book()
            try_weight: float = self.weight + book.weight

            if try_weight > self.max_weight:
                clear()
                print('Passou do peso')
            else:
                self.weight += book.weight
                self.bookcase.loc[len(self.bookcase)] = [book.id, book.author, book.title, book.year, book.weight]  # type: ignore
        else:
            clear()
            print('Estante lotada')


if __name__ == '__main__':
    bookcase = Bookcase(2, 2)
    bookcase.add_book()
    bookcase.add_book()
    bookcase.add_book()
    print(f'{bookcase.bookcase}\nAltura: {bookcase.size}\nPeso máximo: {bookcase.max_weight}Kg\nPeso total: {bookcase.weight}Kg')
