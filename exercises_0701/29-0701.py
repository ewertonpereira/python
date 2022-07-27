"""
Faça um programa que receba 6 números inteiros e mostre:

    * Os números pares digitados
    * A soma dos números pares digitados 
    * Os números ímpares digitados
    * A quantidade de números ímpares digitados
"""
from random import randint

size = 6
array =[]
p = []

while len(array) < size:
    array.append(randint(0,51))


print(list(number for number in array))
print(' ')

print(list(number for number in array if not number % 2))
print(' ')

def sum_even(array):

    sump = 0

    for number in array:
        if not number % 2:
            sump+=number


    return sump

def total_odd(array):

    todd = 0

    for number in array:
        if number % 2:
            todd+=1


    return todd

print(sum_even(array))
print(' ')

print(list(number for number in array if number % 2))
print(' ')
print(total_odd(array))
