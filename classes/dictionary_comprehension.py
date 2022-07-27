"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4) ou 1, 2, 3, 4

Se quisermos criar um set(conjunto):

conjunto = {1, 2, 3 ,4}

Se quisermos criar um dicionário:

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe

{chave: valor for valor in iterável}
[valor for valor in iterável] - lista
"""

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print({chave: valor**2 for chave, valor in numeros.items()})

listanum = [1, 2, 3, 4, 5]

print({valor: valor**2 for valor in listanum})

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

print({chaves[i]: valores[i] for i in range(0, len(chaves))})

# Exemplo com lógica condicional

res = {num:('par' if not num % 2 else 'impar') for num in listanum}
print(res)
