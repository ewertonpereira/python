"""
Leia um vetor com 10 números reais, ordene os elementos deste vetor, e no final escreva 
os elementos do vetor ordenado
"""

from random import uniform

size = 5

def generates_randon_numbers(size: int) -> list:

    array = []
    index = 0

    while index < size:
        array.append(round(uniform(0, 10), 2))
        index+=1


    return array



print(f'Lista: {(result := generates_randon_numbers(size))}')

result.sort()
print(f'Números em ordem crescente: {result}')
result.reverse()
print(f'Números em ordem decrescente: {result}')
print(f'Números em ordem decrescente: {result[::-1]}')
