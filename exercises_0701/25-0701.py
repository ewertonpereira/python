"""
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeoros que são multiplos de 7 ou que terminam com 7.
"""
size = 10
array = []
pattern = 7

while len(array) < size:
    array.append(pattern)
    pattern *= 7


print(list(number for number in array))
