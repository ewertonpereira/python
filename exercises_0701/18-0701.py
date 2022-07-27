"""
Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os múltiplos de um número inteiro x e mostre-os na tela.
"""
import random

size = 10
array = []

while  len(array) < size:
    array.append(random.randrange(1, 15))


print([number for number in array])

mult = int(input('Digite um número inteiro para servir de multiplo: '))

print([number ** mult for number in array])

