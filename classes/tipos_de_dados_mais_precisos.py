"""
Tipos de dados mais precisos

- Literal type
- Union
- Final
- Type dictionaries
- Protocols
"""
from typing import Literal, Union, Final, final, TypedDict, Protocol

# Literal

def pegar_status(user: str) -> Literal['conectado', 'desconectado']:
    pass


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operacao == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operacao == '/':
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}') # !r - Destaca entre aspas simples


calcula_v1('+', 6, 4)
calcula_v1('-', 6, 4)
#calcula_v1('~', 6, 4)


def calcula_v2(operacao: Literal['+', '-', '*', '/'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operacao == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operacao == '/':
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}') # !r - Destaca entre aspas simples


calcula_v2('+', 6, 4)
calcula_v2('-', 6, 4)
#calcula_v2('~', 6, 4)

# Union

def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande'
    else:
        return resultado


# Final

NOME: Final = 'Ewerton'
#print(NOME := 'Ewerton')

# final

"""
@final
class Pessoa:
    pass


class Estudante(Pessoa): # Base class "Pessoa" is marked final and cannot be subclassed
    Pass

    @final
    def estudar(self):
        print(f'Estou estudando')

    
class Estagiario(Estudante):
    pass

    def estudar(self): # Method "estudar" cannot override final method defined in class "Estudante"
        print(f'Estudando e estagiando')
"""
# Typed dictionaries

class CursoPython(TypedDict):
    versao: str 
    atualizacao: int


print(python := CursoPython(versao='3.8', atualizacao=2020))

# Protocols

class Curso(Protocol):
    titulo: str 


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class venda:
    titulo = 'Programação em Python'


estudar(v1 := venda())
