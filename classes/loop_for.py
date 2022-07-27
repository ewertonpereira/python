"""
Loop for

    - Loop -> estrutura de repetição.
    - For -> uma dessas estruturas.

# Python 

for item in interavel:
    //execução do loop
    
Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Explos de iteráveis:
    - String
        nome = 'Ewerton Pereira'
    - Lista
        lista = [1,3, 5, 7,9]
    - Range
        numeros range(1,10)
         
"""
name = 'Ewerton Pereira'

lista = [1,3, 5, 7,9]

numbers = range(1,10) # Temos que transformar em uma lista

# Exemplo de for 1 - iterando sobre um String

for letra in name:
    print(letra)

# Exemplo for 2 - iterando sobre uma lista

for num in lista:
    print(num)
    
# Exmplo for 3 - iterando sobre um range

# range(valor_inicial, valor_final -1)

for num in range(1, 10):
    print(num)

name = 'Ewerton Pereira'
lista = [1,3, 5, 7,9]
numbers = range(1,10)


# Enumerate:
((0, 'E'), (1, 'w'), (...))

for indice, letra in enumerate(name):
    print(name[indice])
    
# OBS: Quando não precisamos de um valor, podemos descartar ele utulizando um underline

for _, letra in enumerate(name):
    print(letra)
    
for valor in enumerate(name):
    print(valor)
"""   
(0, 'E')
(1, 'w')
(2, 'e')
(3, 'r')
(4, 't')
(5, 'o')
(6, 'n')
(7, ' ')
(8, 'P')
(9, 'e')
(10, 'r')
(11, 'e')
(12, 'i')
(13, 'r')
(14, 'a')
    

qtd = int(input('Quantas vezes esse loop deve rolar? '))
sum = 0

for n in range(1, qtd+1):
    num = int(input(f'\nInforme o {n} / {qtd} valor: '))
    sum += num  
print(f'A soma é {sum}\n')
        
for letra in name:
    print(letra, end='') # end= cancela a nova linha automática
    

Tabela de emojis
 
https://apps.timwhitlock.info/emoji/tables/unicode

 - Original: U+1F633
 
 - Modificado: U0001F633
"""
for num in range(1,11):
    print('\U0001F633' * num)
 