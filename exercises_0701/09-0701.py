"""
Crie um program que leia 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos de forma inversa.
"""
import random

vector = []
random.seed()
size = 6
goal = 0

while goal < size:
    number = random.randrange(0,101)
    if number % 2 == 0:
        vector.append(number)
        goal +=1
    
print(vector)
print(vector[::-1])
