"""
Decorators com diferentes assinaturas

Para resolver utilizamos um padrãode projeto cahmado Decorator Pattern.

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.
"""
# Relembrando

def gritar(function):
    def aumentar(nome):
        return function(nome).upper() # Caixa alta em toda função
    return aumentar


# Redecorando com a Decorator Pattern

def gritar_hard(function):
    def aumentar(*args, **kwargs):
        return function(*args, **kwargs).upper() # Caixa alta em toda função
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'


@gritar_hard
def ordenar(principal, acompanhamento):
    return f'Olá! Eu gostaria de um {principal}, acompanhado de {acompanhamento}, por favor'


# Testando

print(saudacao('Ewerton'))

print(ordenar('Hamburguer vegano', 'batata frita'))


@gritar_hard
def lol():
    return 'lol'

print(lol())

# OBS: Vale lembra que podemos utilizar parâmetros nomeados

print(ordenar(acompanhamento='batata frita', principal='CU'))

# Decorator com aargumentos

def verifica_primeiro_argumento(valor):
    def interna(function):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro aargumento precisa ser {valor}'
            return function(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('Rissoles de queijo')
def comida_favorita(*args):
    print(args)
    

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 22))
print(comida_favorita('Rissoles de queijo', 'banana'))
