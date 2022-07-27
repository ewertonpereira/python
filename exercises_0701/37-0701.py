"""
considere um vetor A com 11  elementos onde A1 < A2 < A3 ... < A6 > A7 > A8 ... . A11, ou seja, está ordenando em ordem crescente até o sexto elemento,
e a partir desse elemento está ordenado em descrescente. Dado o vetor da questão  anterior, proponha um algoritmo para ordenasr os elementos.
"""
from random import uniform

size = 11
middle = 6

def generates_randon_numbers(size: int) -> list:

    array = []
    index = 0

    while index < size:
        array.append(round(uniform(0, 10), 2))
        index+=1


    return array


print(f'{(result := generates_randon_numbers(size))}')

def broke_array(array: list) -> list:

    array.sort()
    size: int = len(array)
    index: int = 0
    new: list[float] = []

    for value in array:
        if index < middle:
            new.append(array[index])
            index+=1
        else:
            size-=1
            new.append(array[size])
            

    return new


result.sort()
print(result)
print(f'{(result := broke_array(result))}')