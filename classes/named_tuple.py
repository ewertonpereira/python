"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recap tupla

tuple = (1, 2, 3)
print(tuple[1])

Named Tuple -> São tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros.
"""
from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='vira-lata', nome='Jujuba')
print(ray)

# Acessando os dados 

# Forma 1

print(ray[0]) # Idade
print(ray[1]) # Raça
print(ray[2]) # Nome

# Forma 2

print(ray.idade) # Idade
print(ray.raca) # Raça
print(ray.nome) # Nome

print(ray.index('vira-lata'))
print(ray.count('vira-lata'))
