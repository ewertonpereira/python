"""
Utilizando Lambdas

Conhecidas por expressões lambdas ou simplismente lambda, são unções sem nome, ou seja, funções anônimas.

# Função em Python ex
"""

def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Exemplo de expressão Lambda

lambda x: 3 * x + 1

# Como utilizar expressão lambda?

calc = lambda x: 3 * x + 1
print(calc(4))

# Podemos ter expressões lambidas com multiplas entradas 

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('   ewerton',  ' PEREIra  '))

 # Emfunções em Python podemos ter nenhuma ou várias entradas. Em lambdas tambám

amar = lambda: 'Como não amar Python?'
print(amar())

duas = lambda x, y: (x * y) ** 0.5
print(duas(2, 1))

# OBS: se passarmos mais argumantos do que parâmetros informados teremos TypeError

# Outro exemplo

autores = ['Stephen Hawkinsg', 'Isaac Asimov', 'Yuval Noah Harari', 'Carl Sagan', 'George Orwell']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Função quadrática

# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora(a, b, c):
    """[Retorna a função: f(x) = a * x ** 2 + b * x + c]

    Args:
        a ([type]): [description]
        b ([type]): [description]
        c ([type]): [description]
    """

    return lambda x: a * x ** 2 + b * x + c


teste = geradora(2, 3, -5)

print(teste(0))
print(teste(1)) 
print(teste(2)) 
print(geradora(3, 0, 1)(2))
