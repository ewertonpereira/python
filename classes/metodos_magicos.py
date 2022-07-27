"""
Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam Dunder.

Dunder -> Double Underscore

# dunder init -> __init__

# dunder repr -> __repr__ Representação do objeto

# dunder str -> __str__ 

# dunder len -> __len__

# dunder del -> __del__

# dunder add -> __add__

"""
class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f'O livro {self.__titulo} foi escrito pelo autor {self.__autor}'

    def __str__(self): # str tem prioridade sobre repr
        return self.__titulo

    def __len__(self):
        return self.__paginas

    def __del__(self):
        print(f'Um objeto do tipo Livro foi deletado da memória.')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Colapso', 'Jared Diamond', 653)
livro2 = Livro('Sapiens', 'Harari', 525)

print(livro1)
print(len(livro1))
print(livro1 + livro2)
print(livro1 * '5')
