"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença 
de serem dinâmicas e também de podermos colocar qualquer tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho  e tipo de dado fixo;
    
Em Python:
    - Dinâmico: não possui tamanho fixo;
    - Recebe qualquer tipo de dado;
    
As listas em Pythom são representadas em colchetes '[]'
---------------------
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['E', 'w', 'e', 'r', 't', 'o', 'n', ' ', 'P', 'e', 'r', 'e', 'i', 'r', 'a']

lista3 = []

lista4 = list(range(11))

lista5 = list('Ewerton Pereira')

# Podemos facilmente chegar se determinado valor está contido na lista

num = 8

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')
    
if 'e' in lista5:
    print('Enontrei a letra E!!')
else:
    print('Não ncontrei a letra E')
    
# Podemos facilmente ordenar uma lista

lista5.sort()
print(lista5)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista 

print(lista1.count(1))
print(lista5.count('e'))

# Adicinar elementos em lista 

# OBS: para adicionar elementos em listas, utilizamos e função append()

print(lista1)
lista1.append(47)
print(lista1)

# Com o append nós só conseguimos adicinar um elemento por vez

# lista1.append(12, 35, 69) # Esse comando rertorna um erro.   TypeError: append() takes exactly one argument (3 given)

lista1.append([35, 2, 9]) # Coloca lista como elemento único.
print(lista1)

lista1.extend([123, 56, 99]) # Coloca cada elemento da lista como valor adicional á lista.

print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice.

# OBS: isso não sbustitui o valor inicial, o mesmo será deslocado para a direita da lista.

lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas.

lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista utilizando a função reverse() ou utilizando o slice

# Forma 1

print(lista1)
lista1.reverse()
print(lista1)

# Forma 2
print(lista1[::-1])

# Copindo uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos saber o número de elementos da lista utilizandod a função len()

print(len(lista2))

# Podemos remover facilmente o último elemento de uma lista

print(lista5)
lista5.pop()
print(lista5)

# OBS: O pop não somente o último elemento, mas também o retorna

# Podemos remover um elemento pelo índice

lista5.pop(2)
print(lista5)

# OBS: os elementos á direita desde ínice serão deslocados para a esquerda.

# OBS: se não ouver elemento no índice informado, teremos o erro IndexError.

# Podemos remover todos os elementos 

print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista

nova = [1, 2, 3]
print(nova)
nova *= 3
print(nova)

# Podemos facilemte converter uma string para uma list

# Exemplo 1 

curso = 'Programção em python essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: por padrão o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2

curso = 'Programação, em, python'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python']
print(lista6)

# Abaixo estamos falando: pega lista6, coloca ' '(espaço) em cada elemento e transforma em uma string

curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: pega lista6, coloca '$' em cada elemento e transforma em uma string

curso = '$'.join(lista6)
print(curso)

# Iterando sobre listas

# Exemplo 1 - utilizando for

sum = 0
for elemento in lista1:
    print(elemento)
    sum += elemento
print(sum)

# Exemplo 2 - utilizando while

carrinho = [] # Lista vázia
produto = ''  # Variável string

while produto != 'sair':
    produto = input("Adicione um produto na lista ou digite 'sair' para sair: ")
    if produto != 'sair':
        carrinho.append(produto)
        
for produto in carrinho:
    print(produto)
    
    # Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # Verde
print(cores[1]) # Amarelo
print(cores[2]) # Azul
print(cores[3]) # Branco

# Fazer acesso aos elementos de forma indexada de forma inversa.

# Para entender melhor o ídice negativo, pense na lista como um circulo, onde o final de um elemento está ligado ao início da lista

print(cores[-1]) # Branco
print(cores[-2]) # Azul
print(cores[-3]) # Amarelo
print(cores[-4]) # Verde
#print(cores[-5]) # Erro

-----------------------------------------

for cor in cores:
   print(cor)
    
index = 0
while index < len(cores):
    print(f'{index} ', cores[index])
    index += 1

# Gerar índice em um for - JEITO PYTHÔNICO - certo
 
for index, cor in enumerate(cores):
     print(index, cor)

# Outros métodos não importantes mas também úteis

# Encontrar o índice de um elemento da lista


num = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice da lista está o valor 6?

print(num.index(6))

# OBS: retorna o índece do primeiro elemento encontrado.

# OBS: caso não tenha esse elemento na lista, será aprensetado erro - ValueError
#print(num.index(56))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar e buscar

print(num.index(5, 1)) # Buscando a partirdo índice 1

# Podemos fazer busca dentro de um range, início/fim

print(num.index(8, 3, 6)) # Buscar o elemento 8, entre os índices 3 a 6.

# Revisão slicing

# lista[iníco:fim:passo]
# range(início:fim:passo)

# Trabalhando com o slice de lista com o parâmetro 'início'.

lista = list(range(5))

print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes
print(lista[::]) # Mostra todos os elementos

# Trabalhando com o slice de lista com o parâmetro 'fim'.

print(lista[:2])  # Começa em 0 pega até o índice 2 - 1
print(lista[:4])  # Começa em 0 pega até o índice 4 - 1
print(lista[1:3]) # Começa em 1 pega até o índice 3 - 1

# Trabalhando com o slice de lista com o parâmetro 'passo'.

print(lista[1::2])  # Começa em 1 pega até o final de 2 em 2
print(lista[0::2])  # Começa em 1 pega até o final de 2 em 2

# Invertendo valores em uma lista

name = ['Ewerton', 'Pereira']

name [0], name [1] = name[1], name[0]
print(name)

name.reverse()
print(name)

# Soma*, valor mínimo*, valor máximo*, tamanho

# * Se os valores foram todos interios ou reais

print(sum(lista4)) # Soma
print(max(lista4)) # Máximo
print(min(lista4)) # Mínimo
print(len(lista4)) # Tamanho

# Transformar uma lista em tupla

tupla = tuple(lista4)
print(tupla)
print(type(tupla))

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError

"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['E', 'w', 'e', 'r', 't', 'o', 'n', ' ', 'P', 'e', 'r', 'e', 'i', 'r', 'a']

lista3 = []

lista4 = list(range(11))

lista5 = list('Ewerton Pereira')

cores = ['verde', 'amarelo', 'azul', 'branco']

# Copiando uma lista para outra(Shallow copy e Deep copy)

# Forma 1 - Deep copy

listinha = [1, 2, 3]
new = listinha.copy()
print(new)

new.append(4)
print(listinha)
print(new)

""" Veja que ao utilizarmos listinha.copy() copiamos os dados da listinha para a nova lista,
 mas elas ficaram totalmente independentes, ou seja, modificando uma lista, não afetamos a outra. 
 Isso em Python é chamado de Deep copy."""
 
 # Forma 22 - Shallow copy
 
listinha = [1, 2, 3]
print(listinha)

new = listinha # Cópia
new.append(4)

print(listinha)
print(new)

""" Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista,
mas após realizar modificação e uma das listas, essa modificação se refletiu em ambas as listas, 
isso em Python é chamado de Shallow copy"""
