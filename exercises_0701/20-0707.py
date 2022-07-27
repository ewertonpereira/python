"""
Escreva um programa que leia que leia números inteiros no intervalo de [0-50] e os armazene em um vetor de 10 posições. Preencha um segundo vetor com apenas os números ímpares
do primeiro vetor. Imprima os dois vetores, dois elementos por linha.
"""
import random

size = 10
arrayAll = []
arrayOdd = []
goal = 0

while  goal < size:
    arrayAll.append(random.randrange(0, 50))
    goal += 1


print([number for number in arrayAll])

arrayOdd = [number for number in arrayAll if number % 2]

print([number for number in arrayOdd])

i = 0 # Used by for 2  numbers
j = 2 # Used by for 2  numbers

for _ in arrayOdd:
    if arrayOdd[i:j] != []:
        print(arrayOdd[i:j])
        i += 2
        j += 2


