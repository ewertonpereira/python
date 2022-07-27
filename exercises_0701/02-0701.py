"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre os valores lidos.
"""
values = []
goal = 0

while goal < 6:
    number = int(input(f'Digite 6 números {goal+1}/6: '))
    values.append(number)
    goal +=1
    
print(values)
