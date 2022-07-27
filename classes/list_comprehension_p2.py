"""
List Comprehesion

Nós podemos adicionar estruturas condicionais lógicas às nossas List Compreheension
"""

# Exemplos 

# 1

num = [ 1, 2, 3, 4, 5, 6]

pares = [numero for numero in num if numero % 2 == 0]
impares = [numero for numero in num if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando

# Qualquer número par módulo de 2 é 0, e 0 em Python é False. not False = True

pares = [numero for numero in num if not numero % 2]

# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True

Impares = [numero for numero in num if numero % 2]

print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in num]

print(res)
