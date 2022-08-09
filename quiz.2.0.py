from random import shuffle

question_number: int = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
shuffle(question_number)
lista_escolhas = ['a', 'b', 'c', 'd']
shuffle(lista_escolhas)

perguntas = {
    question_number[0]: {
        'pergunta': 'Quanto é 2 + 2?',
        'alternativas': {
            lista_escolhas[0]: '0',
            lista_escolhas[1]: '1',
            lista_escolhas[2]: '2',
            lista_escolhas[3]: '4'
        },
        'resposta_certa': lista_escolhas[3]
    },
    question_number[1]: {
        'pergunta': 'Quem descobriu a américa?',
        'alternativas': {
            lista_escolhas[0]: 'Pedro Álvares Cabral',
            lista_escolhas[1]: 'Dom Pedro I',
            lista_escolhas[2]: 'Cristóvão Colombo',
            lista_escolhas[3]: 'Bartolomeu Dias'

        },
        'resposta_certa': lista_escolhas[0]
    },
    question_number[2]: {
        'pergunta': 'Qual o nome da galáxia em que está o sistema solar?',
        'alternativas': {
            lista_escolhas[0]: 'Redemoinho',
            lista_escolhas[1]: 'Sombreiro',
            lista_escolhas[2]: 'Andrômeda',
            lista_escolhas[3]: 'Via Láctea'
        },
        'resposta_certa': lista_escolhas[3]
    },
    question_number[3]: {
        'pergunta': 'Quem foi o lateral direito titular do Brasil na copa do mundo 2002?',
        'alternativas': {
            lista_escolhas[0]: 'Belleti',
            lista_escolhas[1]: 'Maicon',
            lista_escolhas[2]: 'Cafu',
            lista_escolhas[3]: 'Daniel Alves'
        },
        'resposta_certa': lista_escolhas[2]
    },
    question_number[4]: {
        'pergunta': 'Quanto é 3 + 5 * 2',
        'alternativas': {
            lista_escolhas[0]: '13',
            lista_escolhas[1]: '10',
            lista_escolhas[2]: '16',
            lista_escolhas[3]: '17'
        },
        'resposta_certa': lista_escolhas[0]
    },
    question_number[5]: {
        'pergunta': 'O tomate é?',
        'alternativas': {
            lista_escolhas[0]: 'Uma leguminosa',
            lista_escolhas[1]: 'Uma fruta',
            lista_escolhas[2]: 'Um tubérculo',
            lista_escolhas[3]: 'Um vegetal'
        },
        'resposta_certa': lista_escolhas[1]
    },
    question_number[6]: {
        'pergunta': 'Qual desses animais não é um mamífero?',
        'alternativas': {
            lista_escolhas[0]: 'Tubarão',
            lista_escolhas[1]: 'Ornitorrinco',
            lista_escolhas[2]: 'Tamanduá',
            lista_escolhas[3]: 'Hipopótamo'
        },
        'resposta_certa': lista_escolhas[0]
    },
    question_number[7]: {
        'pergunta': 'Quantos olhos tem um ciclope na mitologia grega?',
        'alternativas': {
            lista_escolhas[0]: '4',
            lista_escolhas[1]: '3',
            lista_escolhas[2]: '2',
            lista_escolhas[3]: '1'
        },
        'resposta_certa': lista_escolhas[3]
    },
    question_number[8]: {
        'pergunta': 'Quantos estados possui a regição sul do Brasil?',
        'alternativas': {
            lista_escolhas[0]: '4',
            lista_escolhas[1]: '3',
            lista_escolhas[2]: '2',
            lista_escolhas[3]: '1'
        },
        'resposta_certa': lista_escolhas[1]
    },
    question_number[9]: {
        'pergunta': 'As _______ são responsáveis pela produção de energia para todo o orgânismo.',
        'alternativas': {
            lista_escolhas[0]: 'Organélas',
            lista_escolhas[1]: 'Mitocôndrias',
            lista_escolhas[2]: 'Bactérias',
            lista_escolhas[3]: 'Companias elétricas'
        },
        'resposta_certa': lista_escolhas[1]
    },
}
correct_answers: int = 0

for question_key, question_value in sorted(perguntas.items()):
        shuffle(lista_escolhas)
        print(f'{question_key} - {question_value["pergunta"]}')
        for answer_key , answer_value in sorted(question_value['alternativas'].items()):
            print(f'{answer_key} - {answer_value}')

        user_answers: str = input('\nDigite sua escolha: ')

        if user_answers == question_value['resposta_certa']:
            print('\nVocê acertou!')
            correct_answers += 1
        else:
            print(f'\nVocê errou! A resposta certa é : {question_value["resposta_certa"]}')
        print('')


print(f'Percentual de acerto: {(resul := (correct_answers / (number_questions := (len(perguntas))) * 100))} %')
