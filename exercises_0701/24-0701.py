"""
Faça um programa que leia dez conjuntos  de dois valores, o promeiro representando o número do aluno e o segundo representando a sua altura em metros. Encontre o aluno 
mais baixo e o mais alto. Mostre o número do aluno mais baixo e do mais alto, juntamente com suas alturas.
"""
from random import uniform

def func(n):
    mydict = {}
    for i in range(n):
        mydict['Student '+ str(i)] = round(uniform(1.5, 1.9), 2)
    return mydict
 

print(func(10))
print(min(func(10)))
print(max(func(10)))
