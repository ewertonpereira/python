"""
Escreva um program que leia 10 números interios e os armazene em um vetor. Imprima o maior elemento e a posição que ele se encontra.
"""
import random

vector = []
random.seed()
size = 10
goal = 0

while goal < size:
    number = random.randrange(1, 50)
    vector.append(number)
    goal += 1

for index, value in enumerate(vector):
    print(f'Posição: {index}   Valor: {value}')

print(f'\nO valor máximo do vetor é: {max(vector)} e está na posição: {vector.index(max(vector))}')
