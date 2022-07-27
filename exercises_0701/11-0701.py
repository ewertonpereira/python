"""
Faça um programa que preencha um vetor de 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.
"""
import random

vector = []
positive = []
negative = []
random.seed()
size = 10
goal = 0

while goal < size:
    number = random.randrange(-50,50)
    vector.append(number)
    if number < 0:
        negative.append(number)
    elif number > 0:
        positive.append(number)
    goal += 1
    
    
print('--------Vector--------')   
 
for index, value in enumerate(vector):
    print(f'ìndice: {index}  Valor: {value}')
    
    
print('--------positive-------') 

for index, value in enumerate(positive):
    print(f'ìndice: {index}  Valor: {value}')

    
print('--------Negative--------') 

for index, value in enumerate(negative):
    print(f'ìndice: {index}  Valor: {value}')
    
    
print(f'\nA quantidade de números impares é: {len(negative)}')
print(f'A soma dos números pares é: {sum(positive)}')
