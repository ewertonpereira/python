"""
Listas Aninhadas (Nested Lists)

    - Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrys:

        - Unidimensionais (Arrays/Vetores);
        - Multidimensionais(Matrizes);

Em Python nós temos as Listas

numeros = [ 1, 2, 3, 4, 5] 
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(type(listas))
print(listas)

# Como fazemos para acessar os dados?

print(listas[0][1]) # Linha 0 | Coluna 2| # 2
print(listas[2][1]) # Linha 2 | Coluna 2| # 8
print('----------------------------')

# Iterando com Loops em uma lista aninha

for lista in listas:
    for num in lista:
        print(num)


print('----------------------------')

# List Comprehension 

print([numero for numero in listas])
print('----------------------------')

[[print(valor) for valor in lista] for lista in listas]
print('----------------------------')

# Outros exemplos 

# Gerando um tabuleiro/matriz 3 x 3

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1,4)] for j in range(1,4)])
