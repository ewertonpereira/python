"""
Tuplas

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças:

1 - As tuplas são representas por parênteses '()'
2 - As tuplas são imutáveis, isso significa que ao se criar uma tupla ela não muda. 
    Toda operação em uma tupla gera uma nova tupla.
    
    # Cuidado 1: As tuplas representadas por parênteses (), mas veja:

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)

tupla2 = 1, 2, 3, 4, 5
print(tupla2)

# Cuidado 2: Tuplas com um elemento

tupla3 = (42) # Isso não é uma tupla!
print(tupla3)

tupla4 = (4,) # Isso é uma tupla

# Conclusão: podemos concluir que tuplas são definidas pela vírgula e não pelo uso dos parênteses.

tupla5 = 4, # TUPLA

# Podemos gerar uma tupla dinâmicamente com um range(início, fim, passo)

tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tupla

tupla = ('Ewerton', 'Pereira')

first, last = tupla
print(first)
print(last)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar.

# Métdos para adição, remoção de elementos nas tuplas não existem, dado o fato das tuplas seram imutáveis.

# Soma*, valor máximo*, valor mínimo* e tamanho

tupla = tuple(range(11))

print(sum(tupla)) # Soma
print(max(tupla)) # Valor máximo
print(min(tupla)) # Valor mínimo
print(len(tupla)) # Tamanho

# Concatenação de tuplas 

tupla1 = tuple(range(7))
tupla2 = tuple(range(7, 13))
print(tupla1)
print(tupla2)
print(tupla1 + tupla2) # TUPLAS SÃO IMUTÁVEIS

tupla3 = tupla1 + tupla2
print(tupla3)

print(tupla1)
tupla1 +=tupla2
print(tupla1)

# Verificar se determinado elemento está contido em tupla

tupla = tuple(range(56))

print(33 in tupla) # True

# Iterando sobre uma tupla 

tupla = tuple(range(11))

for n in tupla:
    print(n)
    
for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'a', 'b')
print(tupla.count('a'))

name = tuple('Ewerton Pereira')
print(name)
print(name.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas que nãoa precisarmos modificar os dados contidos em uma coleção.

meses = ('Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho')

# O Acesso de elementos de uma tupla também é semelhante a de uma lista

print(meses[1])

# Itererar com while

i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificamos em qual índice  um elemento está na tupla

print(meses.index('Junho'))

# OBS: Caso o elementos não exista, será gerado erro.

# Slicing

print(meses[0:]) # Todos

# Por quê utilizar tuplas?
    - Tuplas são mais rápidas do que listas;
    - Tuplas seu código mais seguro*;      * Isso porque trabalhar com elementos imutáveis traz segurança para o código
    

"""
