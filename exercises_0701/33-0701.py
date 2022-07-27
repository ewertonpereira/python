""" 
Faça um programa que leia um vetor de 15 posições e compacte, ou seja, elimine as posições com valor zero. Para isso, todos os elementos à frente do valor zero, devem ser
movidos uma posição para trás no vetor.
"""
from asyncio.windows_events import NULL
from random import randint as rint

size_vector = 16
vector = []

def show_vector(vector):
    for index, value in enumerate(vector):
        print(f'Index: {index}\tValor: {value}')


while len(vector) < (size_vector):
    vector.append(rint(0, 1))


print('------------------------')


show_vector(vector)

print('------------------------')

def cut_vector(vector):
    for index, value in enumerate(vector):
       if value == 0:
           vector.pop(index)


    return vector

show_vector(cut_vector(vector))

print('------------------------')
