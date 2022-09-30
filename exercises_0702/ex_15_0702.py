"""
Leia uma matriz 5x10 que se refere  respostas de 10 questões de multipla escolha, referentes a 5 alunos. Leia também um vetor de 10 posições contendo o gabarito de
respostas que podem ser a, b, c ou d. Seu programa deverá comparar as respostas de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a 
pontução correspondente a cada aluno.
"""
from typing import List
from os import system


# clean terminal screen
def clear(): 
    return system('cls')

# checks if there are only letters and spaces
def is_alpha_space(str) -> bool:
    return all(char.isalpha() or char.isspace() for char in str )


def check_name() -> str:

    name: str = input('Digite o nome do aluno: \n').title()

    if not is_alpha_space(name):
        clear()
        print('Digite apenas letras!\n')
        name: str = check_name()
    elif len(name) < 3:
        clear()
        print('O nome deve possuir mais de 3 caracteres.\n')
        name: str = check_name()
    
    return name


def check_answer(question_number: int):

    answer: str = input(f'Digite a resposta da questão {question_number}: ').upper()

    if isinstance(answer, str):
        if answer !='A' and answer !='B' and answer !='C' and answer !='D':
            clear()
            print('As opções possíveis são: A, B, C ou D.\n')
            answer: str = check_answer(question_number)
        else:
            return answer



feedback: List[str] = []
names: List[str] = []
school_tests: List[str] = []

students_amount: int = 5
questions_amount: int = 10
question_number: int = 1

clear()
print('Digite as respostas para o gabarito: \n')
for questions in range(questions_amount):
    feedback.append(check_answer(question_number))
    question_number += 1


question_number = 1
clear()
for student in range(students_amount):
    name: str = check_name()
    names.append(name)
    answers: List[str] = []
    clear()
    print('Digite as respostas do aluno: ')
    for questions in range(questions_amount):
        answers.append(check_answer(question_number))
        question_number += 1
    school_tests.append(answers)
    question_number = 1
    clear()

 
result: List[int] = []
adder: int =  0
step: int = 0

for row in range(len(school_tests)):
    for column in range(len(school_tests)):
        if school_tests[row][column] == feedback[step]:
            adder += 1
        step += 1

    result.append(adder)
    adder = 0
    step = 0


clear()
print(title := 'NOTAS\n'.center(29))
for index, value in enumerate(result):
    print(f'Nome: {names[index]}  \nNota: {value}\n')
