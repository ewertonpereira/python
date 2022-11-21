from tools import clear, get_name_person


class Person:

    def __init__(self, name) -> None:
        self.__name: str = name


    def welcome(self, function):
        def get_person():
            print('Olá')
            function()
            print('ler é sempre bom!')
        return get_person


    @welcome
    def get_name_person(self) -> str:
        self.__name: str = input('Digite seu nome: ').strip()
        test = self.__name.replace(' ','')
        if not test.isalpha():
            print('Digite apenas letras: ')
            self.__name: str = get_name_person()
        return self.__name.upper()



if __name__ == '__main__':
    get_name_person()