"""
Teste de velocidade com expressões geradoras


"""
# Genetators

def nums():
    for num in range(1, 11):
        yield num


ge1 = nums()

print(ge1) # Generator

# Generator Expression

ge2 = (num for num in range(1, 11))

print(ge2) # Generation Expression

# Realizando o teste de velocidade

import time

# Generator Expression

gen_ini = time.time()

print(sum(num for num in range(100000)))

gen_tempo = time.time() - gen_ini

# List Comprehension

list_ini = time.time()

print(sum([num for num in range(100000)]))

list_tempo = time.time() - list_ini

print(gen_tempo)
print(list_tempo)
