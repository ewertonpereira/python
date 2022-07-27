"""
List Comprehension

- Utilizando List comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Coprehension

[dado for dado in iteravel]
"""
# Exemplos

num = [1, 2, 3, 4, 5]

res = [number * 10 for number in num]

print(res)

"""
Paraentender melhor o que está acontecendo, devemos dividir a expressão em duas partes:

    - A primeira parte: for number in num
    - A segunda parte: number * 10

"""

res = [number / 2 for number in num]

print(res)

def funcao(valor):
    return valor**2


res = [funcao(number) for number in num]

print(res)

# List Comprehension vs Loop

# Loop

double_number = []

for number in num:
    double_number.append(funcao(number))


print(double_number)

# List Comprehension

print([funcao(number) for number in num])

# Outros exemplos 

# 1

nome = 'ewerton pereira'

print([letra.upper() for letra in nome])

# 2 

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo.title() for amigo in amigos]) # soupica!
print([caixa_alta(amigo) for amigo in amigos])

# 3

print([number * 3 for number in range(1,11)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 2, 3.14]])

# 5

print([str(number) for number in [1, 2, 3, 4, 5]])
