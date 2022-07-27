"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um teste do doctest:

python -m doctest -v nome_do_modulo.py


"""
def soma(a, b):
    """
    Soma os números a e b

    >>> soma(1, 2)
    3
    """
    return a + b


# Outro exemplo, aplicando o TDD

def duplicar(valor):
    """
    Duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]
    """
    return [2 * elemento for elemento in valor]

print(duplicar('ewerton'))

# Erro inesperado...

# OBS: Dentro dodoctest, o Python não reconhece string com aspas duplas. É preciso utilizar aspas simples.

def fala_oi():
    """
    Fala oi

    >>> fala_oi()
    'Oi' # Cuidados com as aspas
    """
    return 'Oi'


# Último caso estranho...

def verdade():
    """
    Retorna verdade

    >>> verdade()
    True # Cuidado com os espaços 
    """
    return True


