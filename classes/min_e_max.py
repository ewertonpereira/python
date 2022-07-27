"""
Min e Max 

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.
"""
#Exemplo

lista = [1, 8, 4, 99, 34, 129]
print(max(lista)) #129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla)) #129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto)) #129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'e': 99, 'e': 34, 'f': 129}
print(max(dicionario)) # f

dicionario = {'a': 1, 'b': 8, 'c': 4, 'e': 99, 'e': 34, 'f': 129}
print(max(dicionario.values())) #129

print(max(3, 33)) # 34

# Faça um programa que receba dois valores do usuário e mostre o maior

# val1 = int(input('Informe o primeiro valor: '))
# val2 = int(input('Informe o segundo valor: '))

# print(max(val1, val2))

print(max(4, 23, 87))

print(max('a', 'b', 'c'))

print(max('a', 'ab', 'abc'))

print(max(3.145, 6.66))

print(max('Ewerton Pereira'))

# min() Retorna o menor valor em umiterável ou o menor de dois ou m ais elementos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista)) #1

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla)) #1

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto)) #1

dicionario = {'a': 1, 'b': 8, 'c': 4, 'e': 99, 'e': 34, 'f': 129}
print(min(dicionario)) # a

dicionario = {'a': 1, 'b': 8, 'c': 4, 'e': 99, 'e': 34, 'f': 129}
print(min(dicionario.values())) #1

print(min(3, 33)) # 3

print(min(4, 23, 87))

print(min('a', 'b', 'c'))

print(min('a', 'ab', 'abc'))

print(min(3.145, 6.66))

print(min('Ewerton Pereira'))

# Outros exemplos:

nomes = ['Ewerton', 'Lauren', 'Fábia', 'Jarbas']

print(max(nomes)) # Ordem alfabética
print(min(nomes)) # Ordem alfabética

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

musicas = [
    {'titulo': 'sic', 'tocou': 9},
    {'titulo': 'Snuff', 'tocou': 2},
    {'titulo': 'Sulfur', 'tocou': 7},
    {'titulo': 'spit it out', 'tocou': 5}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO! Como encontrar a música mais e a menos tocada sem usar max(), min(), e lambda?

max_played = 0
min_played = 999999

for music in musicas:

    if music['tocou'] < min_played:
        min_played = music['tocou']

    if music['tocou'] > max_played:
        max_played = music['tocou']

    
for music in musicas:

    if music['tocou'] == min_played:
        print(music['titulo'])

    if music['tocou'] == max_played:
        print(music['titulo'])
        