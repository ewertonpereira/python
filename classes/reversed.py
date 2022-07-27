"""
Reversed

OBS: Não confunda com a função com a função reverse() que estudamos em listas.

A função reverse() só funciona em listas, já a função reversed() funcona com qualquer iterável;

Sua função é inverter o iterável.

A função reverserd() retorna um iterável chamado List Reverse Iterator
"""
# Exemplos 

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))


# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto 

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto
print(set(reversed(lista))) # Set não define ordem dos elementos 

# Podemos iterar sobre o reversed()

for letra in reversed('Ewerton pereira'):
    print(letra, end='') # Imprime todas aletras na mesma linha


print('\n')

# Podemos fazer o mesmo sem o uso do for

print(''.join(list(reversed('Ewerton Pereira'))))

# Já vimos como fazer isso mais fácil com slide e com strings

print('Ewerton pereira'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso

print(list(n for n in reversed(range(0, 11))))

# Apesar que também já vimos como fazer isso utilizando o próprio range()

print(list(n for n in range(10, -1, -1)))
