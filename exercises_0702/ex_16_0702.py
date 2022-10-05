"""
Faça um programa para corrigir uma prova de 10 questões multipla escolha (a, b, c, d, e), em uma turma com 3 alunos. Cada questão vale 1 ponto. Leia o gabarito, e para cada aluno leia sua matrícula(número inteiro) e suas respostas e sua nota. O percentual de aprovação, assumindo média 7,0.
"""
from filecmp import clear_cache
from os import system


# clean terminal screen
def clear():
    return system('cls')


def get_students_amount() -> int:

    try:
        students_amount: int = int(input('Digite a quantidade de alunos: '))
        if isinstance(students_amount, int):
                return students_amount

    except ValueError:
        clear()
        print('Digite apenas números inteiros!\n')
        students_amount: int = get_students_amount()

    return students_amount


def get_questions_amount() -> int:

    try:
        questions_amount: int = int(input('Digite o números de questões: '))
        if isinstance(questions_amount, int):
            return questions_amount
        
    except ValueError:
        clear()
        print('Digite apenas números inteiros!\n')
        questions_amount: int = get_questions_amount()

    return questions_amount



if __name__ == '__main__':
    clear()
    print(number := (get_students_amount()))
    print(number := (get_questions_amount()))
