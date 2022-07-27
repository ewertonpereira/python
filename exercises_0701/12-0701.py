"""
Faça um programa para ler 5 valor e, em seguida , maostrar todos os valores lidos juntamente com o maior, o menor e a média dos valores.
"""

size = 5
goal = 0
average = 0
array = []

while goal < size:
    number = int(input(f'Digite o número {goal +1}/{size}: '))
    array.append(number)
    average += number
    goal += 1


print(max(array))
print(min(array))

print(average)
print(float(average)/len(array))
