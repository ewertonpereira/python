"""
Leia 10 números e armazene em um vetor V. Crie dois novos vetores V1 e V2. Copie os valores impares para V1 e os pares para V2. Note que cada um dos vetores tem no
máximo 10 elementos, mas nem todos os elementos são utilizados. No final escreva os elementos UTILIZADOS de V1 e V2.
"""
from copy import deepcopy
#from random import randint

v = []
v1 = []
v2 = []
size = 10


def get_user_int_value(array, size):

    while len(array) < size:
        try:
            number = int(input(f'Digite o número {len(array)+1}/{size} para o vetor: '))
            array.append(number)
        except ValueError as err:
            print(f'Digite apenas números inteiros. ERRO: {err}')
        else:
            print([num for num in array])
     

# while len(v) < size:
    # v.append(randint(0,51))

get_user_int_value(v, size)


print([num for num in v])

for number in v:

    copy_number = 0

    if not number % 2:
        copy_number = deepcopy(number)
        v1.append(copy_number)
    else:
        copy_number = deepcopy(number)
        v2.append(copy_number)


print([num for num in v1])
print([num for num in v2])
       
    


