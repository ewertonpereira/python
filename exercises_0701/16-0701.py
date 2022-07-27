"""
Faça um programa que leia um vetor de 5 posições para números reais, e depois, um código inteiro. Se o código for zero, finalize o programa; 
Se for 1 mostre o valor na ordem inversa. Caso o código for diferente de 1 e 2  escreva uma mensagem dizendo que o código esta errado.
"""
import random

size = 5
array = []
goal = 0

while goal < size:
    #random.seed(10)
    array.append(random.uniform(1.0 , 50.0))
    goal += 1


print([round(number, 2) for number in array])

code = int(input('Digite o código: '))

while code != 1 and code != 2:
    code = int(input('Digite o código 1 ou 2: '))


if code == 1:
    print([round(number, 2) for number in array])


if code == 2: 
    print([round(number, 2) for number in array[::-1]])


