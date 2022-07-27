"""
Fazer um programa para ler 5 valores e, em seguida mostrar a posição onde se encontra o maior e o menor valor.
"""
size = 5
goal = 0
array = []

while goal < size:
    number = int(input(f'Digite o número {goal+1}/{size}: '))
    array.append(number)
    goal += 1


arrayMax = max(array)
arrayMin = min(array)

for index, value in enumerate(array):
    if value == arrayMax:
        print(f'O maior valor é {value} e está na posição {index}')
    elif value == arrayMin:
        print(f'O menor valor é {value} e está na posição {index}')


