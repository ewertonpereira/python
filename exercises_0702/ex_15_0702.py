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
        print('Digite apenas letras.')
        answer: str = get_answer(question)


def get_answer(question: int):
    answer: str = check_answer(input(f'Digite a resposta da questão {question}: ').upper(), question)
    return answer
    

question = 1
while question <= 10: 
    get_answer(question)
    question += 1



