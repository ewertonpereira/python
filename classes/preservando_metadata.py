"""
Preservando metadatas com wraps

Metadados -> São dados intrínsecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.

"""
# Problema

def ver_log(function):
    def logar(*args, **kwargs):
        """[Eu sou uma função(logar) dentro de outra]"""       
        print(f'Você está chamando {function.__name__}')
        print(f'Aqui a documentação: {function.__doc__}')
        return function(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dos números"""
    return a + b


# print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)

# Resolução do problema

from functools import wraps

def ver_log2(function):
    @wraps(function) # Isto resolve o problema
    def logar(*args, **kwargs):
        """[Eu sou uma função(logar) dentro de outra]"""       
        print(f'Você está chamando {function.__name__}')
        print(f'Aqui a documentação: {function.__doc__}')
        return function(*args, **kwargs)
    return logar


@ver_log2
def soma2(a, b):
    """Soma dos números"""
    return a + b


# print(soma(10, 30))

print(soma2.__name__)
print(soma2.__doc__)