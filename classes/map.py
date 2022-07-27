"""
Map

Com Map fazemos mapeamento de valores para função.
"""
import math

def area(r):
    """[Calcula a area de um circulo com raio r]

    Args:
        r ([type]): [description]
    """

    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [1, 5, 7.1, 0.3, 10, 44]

# Forma comum 

areas = []

for r in raios:
    areas.append(area(r))


print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: o primeiro a função e o segundo um iterável. Retorna um map object

areas = map(area, raios)
print(list(areas))

# Forma 3 - Map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))
"""
OBS: Após a primeira utilização da função map() ela zera.

Para fixar - Map 

Temos dados iteráveis:

dados: a1, a2,...,an

Temos uma função:

Função: f(x)

Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

O map object: f(a1), f(a2), f(...), f(n)

"""

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Beunos Aires', 19), ('Los Angeles', 26), ('Tokio', 27)]
print(cidades)

# f = 9/5 * c + 32

# Lambida

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
