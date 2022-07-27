"""
Faça um programa para ler a nota da prova de 15 alunos reais e armazene num vetor, calcule e imprima a média geral.
"""
vector = []
size = 3
goal = 0
average = 0

while goal < size:
    number = float(input(f'Digite a nota do aluno {goal +1}/{size}: '))
    vector.append(number)
    average += number
    goal += 1

print('\nTabela de alunos e notas\n')

for index, value in enumerate(vector):
    print(f'Aluno: {index+1}  Nota: {value}')


print(f'\nA média final da turma é: {round((average/3),2)}') # round é usado para poder definir o número de casas decimais
