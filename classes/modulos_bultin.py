"""
Trabalhando com Módulos Bult in(módulos integrados, que já vem instalados no Python)

|Python|Módulos bultin|
"""
# Utilizando alias(apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas a funções de um módulo utilizando o *

from random import *

# Importando todo o módulo

from random import randint as rdi, random as rdm

print(rdi(5, 99))
print(rdm())

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(0, 10))
lista = ['Ewerton','Pereira', 'Santos']
print(shuffle(lista))
print(lista)
print(choice('Ewerton'))
