import pandas as pd
from Book import Book
from datetime import datetime

height = 2
weight = 0
max_weight = 10

df = pd.DataFrame(columns=['ID', 'Autor', 'Título', 'Ano', 'Peso'])

def add_book(df, height, weight, max_weight):
    if len(df) <= (height - 1):
        book = create_book()
        weight += book.weight
        if weight > max_weight:
            return 'passou do peso'
        else:
            df.loc[len(df)] = [book.id, book.author, book.title, book.year, book.weight]
    else:
        return 'Estante lotada'
        
    return weight

def create_book():
    author = input('Digite o autor: ')
    title = input('Digite o título: ')
    year = int(input('Digite o ano: '))
    weight = float(input('Digite o peso: '))
    book = Book(author,title, year, weight)

    return book

#weight = add_book(df, height, weight, max_weight)
#weight = add_book(df, height, weight, max_weight)
#weight = add_book(df, height, weight, max_weight)

print(df)
print(weight)
# book = create_book()
# print(book.id, book.author, book.title, book.year, book.weight)
print(result := datetime.today().year)
print(type(result))
