"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.
"""
import random
from itertools import groupby

size = 10
array = []
goal = 0

while goal < size:
    number = random.randrange(1,10)
    array.append(number)
    goal += 1


print(array)

for number in groupby(sorted(array)):
    print(f'Valor {number[0]}    número de aparições {len(list(number[1]))}')
    

