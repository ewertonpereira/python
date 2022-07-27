"""
Faça um programa que leia um vetor de 8 posições  e, em seguida, leia também dois valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa 
deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.
"""
vector = []
size = 10
sizetwo = 2
goal = 0
total = 0

print('------SOMANDO VALORES ESPECÍFICOS DE UMA LISTA------\n')

while goal < size:
    number = int(input(f'Digite {size} valores {goal+1}/{size}: '))
    vector.append(number)
    goal += 1

print('\nQuadro de posições e valores\n')

for index, value  in enumerate(vector):
    print(f'Posição: {index}  Valor: {value}')
    
goal = 0

while goal < sizetwo:
    number = int(input(f'\nEscolha a posição de {sizetwo} valores da lista para serem somados {goal+1}/{sizetwo}: '))
    total += vector[number]
    goal += 1
    
print(f'A soma dos {sizetwo} é: {total}')
