from person import Person
from tools import get_author_book
from uuid import UUID, uuid4


class Author(Person):
    
    def __init__(self, name: str):
        self.id: UUID = uuid4()
        super().__init__(name)
        

    def get_author_name(self):
        return self._Person__name.title()  # type: ignore


    # def __str__(self) -> str:
    #     return f'Autor: {self._Person__name.title()}\n' # type: ignore

        
if __name__ == '__main__':
    baleia = Author(get_author_book())
    print(baleia.get_author_name())