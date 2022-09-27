"""
Leia uma matriz 5x10 que se refere  respostas de 10 questões de multipla escolha, referentes a 5 alunos. Leia também um vetor de 10 posições contendo o gabarito de
respostas que podem ser a, b, c ou d. Seu programa deverá comparar as respsotas de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a 
pontução correspondente a cada aluno.
"""
def check_answer(answer: str, question: int):
    if isinstance(answer, str):
        if answer !='A' or answer !='B' or answer !='C' or answer !='D':
            answer: str = get_answer(question)
        else:
            return answer
    else:
        answer: str = get_answer(question)


def get_answer(question: int):
    answer: str = input(f'Digite a resposta da questão {question}: ').upper()
    check_answer(answer)
    


def answers():


word = 'boi'
word = isinstance(word, str)
print(word)
