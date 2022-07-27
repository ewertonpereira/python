"""
Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores, guardando-os num vetor. Ordene o valor assim que for digitado. Mostre ao final na tela os valores em ordem.
"""


size: int = 10
array: list = []
index: int = 0

while index < size:
    number: int = int(input('Digite um nímero inteiro: '))
    array.append(number)
    array.sort()
    index+=1


print(array)


