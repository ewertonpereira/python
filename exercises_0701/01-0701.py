"""
Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os seguintes passos:

    - Atribua os seguintes valores ao vetor: 1, 0, 5, -2, -5, 7.
    - Armazene em uma variável inteira(simples) a soma entre os valores das posições A[0], A[1] e A[5] e mostre a soma.
    - Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
    - Mostre na telacada valor do vetor A, um em cada linha.
"""
a = []
number = ''
goal = 0

while goal < 6:
    number = int(input(f'Digite um número {goal+1}/6: '))
    a.append(number)
    goal +=1  
    
print(a)
print(' ')

elements_sum = a[0] + a[1] + a[5]
print(f'A soma de {a[0]} + {a[1]} + {a[5]} é: {elements_sum}')
print(' ')

a[3] = 100
print(a)
print(' ')

for index in enumerate(a):
    print(index)
