"""
Sorted

OBS: não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort() só 
funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome já diz, sorted() serve para ordenar.

OBS: o sorted() SEMPRE retona uma lista com os elementos do iterável ordenaos.
"""

# Exemplo

numeros = [6,1,8,6]

print(numeros)
print(sorted(numeros)) # Ordenar do menor para o maior
print(numeros)

# Adicionando  parâmetros ao sorted()

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor


# Podemos utilizar o sorted() para coisas mais complexas

user = [
    {'username':'ewerton', 'tweets':['Metal is the law', '#forabolsonaro']},
    {'username':'julia', 'tweets':['Me gusta marijuana', '#forabolsonaro']},
    {'username':'kerlen', 'tweets':['#forabolsonaro']},
    {'username':'paulinho', 'tweets':[]},
    {'username':'tonho', 'tweets':['#forabolsonarogenocida', '#forabolsonaro']},
]

print(sorted(user, key=len))

print('---------------------------------------------------------------------------------------')


# Ordenando  por username - Ordem Alfabética

print(sorted(user, key=lambda user: user["username"])) # reverse=True

print('---------------------------------------------------------------------------------------')

# Ordenando pelo nhúmero de tweets

print(sorted(user, key=lambda user: len(user["tweets"])))

print('---------------------------------------------------------------------------------------')
# Último exemplo 

musicas = [
    {'titulo': 'sic', 'tocou': 8},
    {'titulo': 'Snuff', 'tocou': 2},
    {'titulo': 'Sulfur', 'tocou': 8},
    {'titulo': 'spit it out', 'tocou': 5}
]

# Ordena da menos tocada para a mais tocada

print(sorted(musicas, key=lambda musica: musica['tocou']))
