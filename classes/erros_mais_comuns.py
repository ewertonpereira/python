"""
Erros mais comuns em Python

ATENÇÃO!!! É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

OS erros mais comuns 

1 - SyntazError -> Ocorre quando o Python encontra um erro de sixtaxe. Ou seja, você escreveu algo que 
o Python não reconhece como linguagem.

# Exemplos SyntaxError

a)

# def funcao: # Faltam os "()"
   # print('EWerton')

b)

# None = 1 #  cannot assign to None

2 - NameError -> Ocorre quando a variável ou função não foi definida.

# Exemplos NameError

print(ewerton) # name 'ewerton' is not defined

3 - TypeError -> Ocorre quando uma ação/operação/função é aplicada a um tipo errado

4 - IndexError -> Ocorre qunado tentamos acessar um elemento em uma lista ou outro tipo de dado 
indexado utilizando um índice inválido.

5 - ValueError -> Ocorre quando uma função /opereção buily-in (integrada) recebe um argumento com tipo
correto mas valor inapropriado.

6 - KeyError - Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços).
"""