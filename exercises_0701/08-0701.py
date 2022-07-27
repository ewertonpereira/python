"""
Crie um program que leia 6 valores inteirose, em siguida, mostre na tela os valores lidos na ordem inversa.
"""
import random

vector = []
random.seed()
size = 6
goal = 0

while goal < size:
    number = random.randrange(1, 201)
    vector.append(number)
    goal += 1
    
print(vector)
vector.reverse() # Usando reverse()
print(vector)
print(vector[::-1]) # Usando slicing
