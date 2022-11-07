from uuid import UUID, uuid4


class Book:

    def __init__(self, author: str, title: str, year: int, weight: float):
        self.id: UUID = uuid4()
        self.author: str = author
        self.title: str = title
        self.year: int = year
        self.weight: float = weight


if __name__ == '__main__':
    pass
    # book = Book('harari', 'sapiens', 2010, 1.32)
    # print(f'ID: {book.id}\nAutor: {book.author}\nTítulo: {book.title}\nAno: {book.year}\nPeso: {book.weight}')
    # print(type(book.id))
