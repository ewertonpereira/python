import pandas as pd
from person import Person
from uuid import UUID, uuid4


class Client(Person):

    def __init__(
            self, 
            name: str, 
            email: str, 
            address: str, 
            birth_date: str
        ) -> None:

        self.__historic = pd.DataFrame(columns=['Livro', 'Data'])
        self.__id: UUID = uuid4()
        super().__init__(name)
        self.__email = email
        self.__address = address
        self.__birth_date: str = birth_date