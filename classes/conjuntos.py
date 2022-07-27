"""
Conjuntos

 Conjuntos em qualquer linguagem de programação, estamos fazendo referência à teoria dos conjuntos 
 da matemárica.
 
 Aqui no Python os cojuntos são chamados de Sets.
 
 Dito isso da mesma forma que na matemática:
    - Sets(conjuntos) não possuem valores duplicados;
    - Sets(conjuntos) não possuem valores ordenados;
    - Elementos não são acessado via índice, ou seja, conjuntos não são indexados.
    
Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas nos importamos com a 
ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (Sets) são refênciados em Python com '{}'.

Diferênça entre conjuntos(Sets) e mapas(dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor.

# Definindo um conjunto
"""
# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos
print(s)

# OBS: ao criar um conjunto, caso seja adicionado um valor já existe, o mesmo será ignorado  semgerar erro e não fará parte do conjunto

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 6}
print(s)

# Podemos se determinado elemento esta contido no conjunto.

num = 13
if num in s:
    print(f'Tem o {num}')
else:
    print(f'Não tem o {num}')

# Tmportante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 8 elementos
lista = [99, 2, 23, 6, 13, 74, 2, 6]
print(f'Lista: {lista} com {len(lista)} e elementos')

# Tuplas aceitam valores duplicados, então temos 8 elementos
tupla = (99, 2, 23, 6, 13, 74, 2, 6)
print(f'Tulpla: {tupla} com {len(tupla)} e elementos')

# Dicionários não aceitam chaves duplicadas, então temos 6 elementos
dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} e elementos')

# Conjuntos não aceitam valores duplicados, então temos 6 elementos
conjunto = {99, 2, 23, 6, 13, 74, 2, 6}
print(f'Conjunto: {conjunto} com {len(conjunto)} e elementos')

# Assim como todo outro conjunto Python podemos colocar ttipos de dados misturados em Sets

s = {1, 'b', True, 34.56, 44}
print(type(s))

# Podemos iterar em um Set normalmente

for valor in s:
    print(valor)

# Usos interessantes com Sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou um museu e os visitantes informam manualmente a cidade de onde vieram. 
# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo horizonte', 'São Paulo', 'Porto Alegre', 'Rio de Janeiro', 'Porto Alegre', 'São Paulo' ]
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? Faria um loop na lista...?

print(len(set(cidades)))

s = {1, 2, 3}
s.add(4)
s.add(4) # Dulicidade não gera erro. Simplismente é ignorado e não é adicionado.
print(s)

# Remover elementos em um conjunto

# Forma 1

s = {1, 2, 3, 4}
s.remove(4) # Não é índice! Informamos o valor a ser removido.
print(s)

# OBS: Caso o valor não seja encontrado, será gerado KeyError. Nenhum valor é retornado.

# Forma 2

s.discard(2)
print(s)

# OBS: Se o valor não for encontrado, nenhum erro é gerado.

# Copiando um conjunto para outro

s = {1, 2, 3, 4, 5}

# Forma 1 - Deep copy

novo = s.copy()

# Forma 2 - Shallow copy

new = s

# Podemos todos os itens de um conjunto

s = {1, 2, 3, 4}
print(s)

s.clear()
print(s)

# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes de Python e um com estudantes de Java.

est_python = {'Marcos', 'Ewerton', 'Kérlen', 'Zé'}
est_java = {'Laura', 'Maurício', 'Ewerton', 'Rafael', 'Kérlen'}

# Veja que alguns que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

uniao = est_python.union(est_java)
print(uniao)

# Forma 2 - Utilizando o caractere pipe '|'

uniao2 = est_python | est_java
print(uniao2)


# Gerar um conjunto de estudantes que estam em ambos os cursos

# Forma 1 - Utilizando o intersection

ambos = est_python.intersection(est_java)
print(ambos)

# Forma 2 - Utilizando o '&'

ambos2 = est_python & est_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão em ambos os cursos

python = est_python.difference(est_java) # Os que só estudam Python
print(python)
java = est_java.difference(est_python)   # Os que só estudam Java
print(java)

# Soma*, valor máximo*, valor mínimo*, tamanho

s = {1, 2, 3, 6, 56}

print(sum(s)) # Soma
print(max(s)) # Valor máximo
print(min(s)) # Valor mínimo
print(len(s)) # Tamanho
