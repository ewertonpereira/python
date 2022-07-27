"""
Faça um programa que receba do usuário um vetor de 10 posições. Em seguida deverá ser impresso o maior e o menor valor do vetor.
"""
import random

vector = []
goal = 0
size = 10
random.seed()

while goal < size:
    number = random.randrange(1, 101)
    vector.append(number)
    goal += 1
    
for index, value in enumerate(vector):
    print(f'Índice: {index} Valor {value}')
    
print(f'\nO valor máximo do vetor é: {max(vector)}')
print(f'O valor mínimo do vetor é: {min(vector)}')
