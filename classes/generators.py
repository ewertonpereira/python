"""
Generators Expression

Em aulas anteriores n´s estudamos:
    _ List Comprehension;
    - Dictionary Comprehension;
    - Set Comprehension;

Não vimos:
    Tuple Comprehension... porque elas se chamam Generators

    nomes = ['Caelos', 'Camila', 'Cassiano', 'Vanessa']

    print(any([nome[0]] == 'C' for nome in nomes))
"""


# Poderíamos ter feito utilizando generators

from sys import getsizeof

nomes = ['Carlos', 'Camila', 'Cassiano', 'Vanessa']

print(any([nome[0] == 'C'for nome in nomes]))

# List COmprehension

res = [nome[0] == 'C'for nome in nomes]
print(type(res))

# Generator

res = (nome[0] == 'C'for nome in nomes)
print(type(res))

# Qual é a função de getsizeof()? -> Retorna a quantidade de bits em memória do elemento passado como parâmetro

# Mostra quantos bytes a string 'Ewerton' está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Ewerton'))
print(getsizeof('Ewerton Pereira'))
print(getsizeof(4))
print(getsizeof(9990))
print(getsizeof(99999999999))
print(getsizeof(True))

# Gerando uma lista de de números com List Comprehension

list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de de números com Set Comprehension

set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de de números com Dictionary Comprehension

dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de de números com Generators

gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Dict Comprehension: {dict_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Genetator Expression: {gen} bytes')

# Eu posso iterar no Generator Expression? Sim!

gene = (x * 10 for x in range(1000))
print(gene)
print(type(gene))

#for num in gene:
    #print(num)

print(list(num for num in gene))


