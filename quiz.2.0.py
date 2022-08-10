"""
O algoritmo abaixo foi desenvolvido com o intuito de representar uma prova múltipla escolha.

Características:
    - Randomizar a ordem de exibição das questões a cada execução;
    - Randomizar a ordem de exibição das alternativas de cada questão a cada execução;
    - Receber a opção da alternativa escolhida pelo usuário;
    - Possibilida ao usuário sair do programa a qualquer momento;
    - Checar e mostrar a resposta correta;
    - Mostrar o percentual de acertos do usuário
    - Possibilita o usuário tentar o questionário novamente
"""
from random import shuffle

def quiz() -> None:

    answer: bool = False
    user_answer: str = ''

    print('=' * 90)
    print(title := 'MENU PRINCIPAL'.center(90))
    print('=' * 90)

    while not answer:
        user_answer: str = input('\nDigite [1] para começar o questionário ou [0] para sair: ')
        if user_answer == '0' or user_answer == '1':
            answer = True


    match user_answer:
        case '1':

            print('')
            print('=' * 90)
            print(title := 'QUESTIONÁRIO'.center(90))
            print('=' * 90)
            question_number: int = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
            shuffle(question_number)
            list_choices:list[str] = ['a', 'b', 'c', 'd']
            shuffle(list_choices)

            questions = {
                question_number[0]: {
                    'question': 'Quanto é 2 + 2?',
                    'alternatives': {
                        list_choices[0]: '0',
                        list_choices[1]: '1',
                        list_choices[2]: '2',
                        list_choices[3]: '4'
                    },
                    'correct_answer': list_choices[3]
                },
                question_number[1]: {
                    'question': 'Quem descobriu a América?',
                    'alternatives': {
                        list_choices[0]: 'Pedro Álvares Cabral',
                        list_choices[1]: 'Dom Pedro I',
                        list_choices[2]: 'Cristóvão Colombo',
                        list_choices[3]: 'Bartolomeu Dias'

                    },
                    'correct_answer': list_choices[0]
                },
                question_number[2]: {
                    'question': 'Qual o nome da galáxia em que está o sistema solar?',
                    'alternatives': {
                        list_choices[0]: 'Redemoinho',
                        list_choices[1]: 'Sombreiro',
                        list_choices[2]: 'Andrômeda',
                        list_choices[3]: 'Via Láctea'
                    },
                    'correct_answer': list_choices[3]
                },
                question_number[3]: {
                    'question': 'Quem foi o lateral direito titular do Brasil na copa do mundo 2002?',
                    'alternatives': {
                        list_choices[0]: 'Belleti',
                        list_choices[1]: 'Maicon',
                        list_choices[2]: 'Cafu',
                        list_choices[3]: 'Daniel Alves'
                    },
                    'correct_answer': list_choices[2]
                },
                question_number[4]: {
                    'question': 'Quanto é 3 + 5 * 2',
                    'alternatives': {
                        list_choices[0]: '13',
                        list_choices[1]: '10',
                        list_choices[2]: '16',
                        list_choices[3]: '17'
                    },
                    'correct_answer': list_choices[0]
                },
                question_number[5]: {
                    'question': 'O tomate é?',
                    'alternatives': {
                        list_choices[0]: 'Uma leguminosa',
                        list_choices[1]: 'Uma fruta',
                        list_choices[2]: 'Um tubérculo',
                        list_choices[3]: 'Um vegetal'
                    },
                    'correct_answer': list_choices[1]
                },
                question_number[6]: {
                    'question': 'Qual desses animais não é um mamífero?',
                    'alternatives': {
                        list_choices[0]: 'Tubarão',
                        list_choices[1]: 'Ornitorrinco',
                        list_choices[2]: 'Tamanduá',
                        list_choices[3]: 'Hipopótamo'
                    },
                    'correct_answer': list_choices[0]
                },
                question_number[7]: {
                    'question': 'Quantos olhos tem um ciclope na mitologia grega?',
                    'alternatives': {
                        list_choices[0]: '4',
                        list_choices[1]: '3',
                        list_choices[2]: '2',
                        list_choices[3]: '1'
                    },
                    'correct_answer': list_choices[3]
                },
                question_number[8]: {
                    'question': 'Quantos estados possui a regi1ão sul do Brasil?',
                    'alternatives': {
                        list_choices[0]: '4',
                        list_choices[1]: '3',
                        list_choices[2]: '2',
                        list_choices[3]: '1'
                    },
                    'correct_answer': list_choices[1]
                },
                question_number[9]: {
                    'question': 'As _______ são responsáveis pela produção de energia para todo o orgânismo.',
                    'alternatives': {
                        list_choices[0]: 'Organélas',
                        list_choices[1]: 'Mitocôndrias',
                        list_choices[2]: 'Bactérias',
                        list_choices[3]: 'Companias elétricas'
                    },
                    'correct_answer': list_choices[1]
                },
            }
            correct_answers: int = 0

            for question_key, question_value in sorted(questions.items()):
                    shuffle(list_choices)
                    print(f'{question_key} - {question_value["question"]}')
                    for answer_key , answer_value in sorted(question_value['alternatives'].items()):
                        print(f'{answer_key} - {answer_value}')

                    user_answers: str = input('\nDigite uma das alternativas ou digite [s] para sair: ').lower()
                    if user_answers == 's':
                            exit()

                    while user_answers != 'a' and user_answers != 'b' and user_answers != 'c' and user_answers != 'd' and user_answers != 's':
                        user_answers: str = input('\nDigite uma das alternativas [a - b - c - d] ou digite [s] para sair: ').lower()
                        if user_answers == 's':
                            exit()


                    if user_answers == question_value['correct_answer']:
                        print('\nVocê acertou!')
                        correct_answers += 1
                    else:
                        print(f'\nVocê errou! A resposta certa é : {question_value["correct_answer"]}')
                    print('')


            print(f'Percentual de acerto: {(resul := (correct_answers / (number_questions := (len(questions))) * 100))} %')
            
            print('=' * 90)
            print(title := 'Created by Ewerton Pereira'.center(90))
            print('=' * 90)

            answer = False

            while not answer:
                user_answer: str = input('\nDigite [1] se deseja reiniciar o questionário ou [0] para sair: ')
                if user_answer == '0' or user_answer == '1':
                    answer = True


            match user_answer:
                case '1':
                    quiz()
                case '2':
                    exit()


        case '2':
            exit()


if __name__ == '__main__':
    quiz()
