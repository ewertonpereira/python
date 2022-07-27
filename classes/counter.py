"""
Módulo collections - Counter

https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performance Container Datatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com 
com um dicionário, contendo como chave o elemento da listapassada como parâmetro e como valor 
a quantidade de ocorrência desse elemento.

# Realizando o import

from collections import Counter

# Podemos qualquer iterável, aqui usamos uma lista.

# Exemplo 1

lista = [1, 1, 1, 2, 2, 3, 3, 6, 5, 4 , 5 , 1 ,1, 3 ,5]

# Utilizando o Counter

res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 3: 3, 5: 3, 2: 2, 6: 1, 4: 1})

# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.


# Exemplo 2

print(Counter('Ewerton Pereira'))

"""
from collections import Counter

# Exemplo 3

texto = """
Python foi criado no final dos anos oitenta(1989) por Guido van Rossum no Centro de Matemática e 
Tecnológia da Informação (CWI, Centrum Wiskunde e Informatica), na Holanda, como sucessor da 
linguagem de programação ABC, capaz de lidar com exceções e interagir com o sistema operacional Amoeba.
O nome da língua vem do gosto de seu criador pelos humoristas britânicos Monty Python. 
Van Rossum é o principal autor de Python, e seu papel central contínuo na decisão da direção 
de Python é reconhecido, referindo-se a ele como Ditador de Vida Benevolente.
Python é uma linguagem de programação interpretada cuja filosofia enfatiza uma sintaxe 
favorecendo um código mais legível, além de ser “free”.
"""
palavras = texto.split()
# print(palavras)
res = Counter(palavras)
print(res)

# Encontrando as 5 palavas com mais ocorrênci no texto.

print(res.most_common(5))
