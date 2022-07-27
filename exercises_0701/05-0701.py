"""Leia um vetor de 10 posições, contar e escrever quantos números pares ele possui."""
import random

vector = []
size = 10
goal = 0
sumx  = 0
random.seed()

while goal < size:
    number = random.randrange(1, 25)
    vector.append(number)
    goal += 1
    
print('--------Vector--------\n')

for index, value  in enumerate(vector):
    if (value % 2) == 0: 
        print(f'Posição: {index}  Valor: {value}')
        sumx += 1
        
print(f'\nTotal de números pares: {sumx}')
