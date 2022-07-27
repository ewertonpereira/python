"""
Faça um vetor de 50 posições preenchido com com o seguite valor (i + 5 * i) % (i + 1), sendo i a posição do elemento no vetor. Em seguida mostre na tela.
"""
size = 10
array = []
goal = 0

while  goal < size:
    array.append((goal + 5 * goal) % (goal + 1))
    goal += 1


print([number for number in array])
