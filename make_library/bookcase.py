import pandas as pd
from Book import Book
from 

class Bookcase:

    

    def __init__(self,height, max_weight) -> None:
        #pd.set_option('display.max_rows', width)
        #pd.set_option('display.max_columns', height)
        self.bookcase = pd.DataFrame(columns=['ID', 'Autor', 'Título', 'Ano', 'Peso'])
        self.size: int = size
        self.max_weight: float = max_weight
        self.weight: float = 0
        

    def add_book(self) -> None:
        clear()
        if len(self.bookcase) <= (self.size - 1):
            book = create_book()
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
    #print(bookcase.bookcase)
    print(f'{bookcase.bookcase}\nAltura: {bookcase.size}\nPeso máximo: {bookcase.max_weight}Kg\nPeso total: {bookcase.weight}Kg')
