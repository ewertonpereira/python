import pandas as pd
import Book


class Bookcase:

    

    def __init__(self,height, max_weight) -> None:
        #pd.set_option('display.max_rows', width)
        #pd.set_option('display.max_columns', height)
        self.bookcase = pd.DataFrame(columns=['ID', 'Autor', 'Título', 'Ano', 'Peso'])
        self.height = height
        self.max_weight = max_weight
        self.weight = 0
        

    def add_book(self):
        self.bookcase.loc[len(bookcase)] = ['harari', 'sapiens', 2010, 1.32]
        #self.weight += book.weight


if __name__ == '__main__':
    bookcase = Bookcase(5, 5, 50)
    Bookcase.add_book
    print(f'Data: {bookcase.bookcase}\nAltura: {bookcase.height}\nLargura: {bookcase.width}\nPeso máximo: {bookcase.max_weight}\nPeso: {bookcase.weight}')

    
