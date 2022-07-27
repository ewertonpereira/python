"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes desse vetor, armazenando o resultado em outro vetor.
Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
"""
vector1 = []
vector2 = []
goal = 0
size = 3

while goal < size:
    number = float(input(f'Digite {size} valores para acrescentar ao vetor {goal+1}/{size}: '))
    vector1.append(number)
    goal += 1
    
print(vector1)

goal = 0
while goal < size:
    pow = vector1[goal] ** 2
    print(pow)
    vector2.append(pow)
    goal += 1
    
print(vector2)
