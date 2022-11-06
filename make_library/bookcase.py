from typing import Bool
import pandas as pd
import Book


class Bookcase:

    

    def __init__(self,height, width, max_weight) -> None:
        self.bookcase = pd.DataFrame()
        self.height = height
        self.width = width
        self.max_weight = max_weight
        self.weight = 0
        

    def check_space(self) -> Bool:
        pass

    def add_book(self, book: Book):
        self.weight += book.weight


if __name__ == '__main__':
    pass