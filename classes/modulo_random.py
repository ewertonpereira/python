"""
Módulo Random e o que são módulos

Em Python, módulos nada mais são do que outros arquivos Python

Módulo Random -> Possui várias funções para geração de números psedo-aleatório.

# OBS: Existem duas formas de se utilizar um módulo ou função desde

# Forma 1 - Importando todo o módulo

# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que 
estiverem dentro do módulo ficarão disponíveis(ficarão em memória). Caso você saiba quais as funções você 
precisa utilizar deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor
na forma 2.

random() -> Gera um número real pseudo-aleatório entre 0 e 1
"""
# import random

# print(random.random())

"""
# OBS: Veja uqe para utilizara  função random() do pacote random, nós colocamos o nome do pacote e o nome
da função, separados por "."

OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é 
apenas uma das funções de random.

"""
# Forma 2 - Importando uma função especcífica do módulo(forma recomendada)

from random import random, uniform, randint, choice, shuffle

# No import a cima estamos falanado: Do módulo random importe a função random

for i in range(10):
    print(random())


print(list(random() for num in range(10)))

# uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos

print(list(uniform(3, 7) for num in range(10))) # 7 não é incluido

# randint() -> Gera valores inteiros pseudo-aleatótios entre os valores estabelecidos.

# Gerador de apostas para a mega-sena

for i in range(6):
    print(randint(1, 61), end=', ') # Começa em 1 e vai até 60


# choice() -> Mostra um valor aleatório entre um iterável.

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

# shuffle() -> Tem a função de embaralhar dados

cartas = ['k', 'q', 'j', 'a']

print(cartas)
shuffle(cartas)
print(cartas)
print(cartas.pop())
