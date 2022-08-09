from random import shuffle

question_number: int = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
#shuffle(question_number)

perguntas = {
    question_number[0]: {
        'id': 1,
        'pergunta': 'Quanto é 2 + 2?',
        'alternativas': {
            

        },
        'resposta_certa': '4'
    },
    question_number[1]: {
        'id': 2,
        'pergunta': 'Quanto é 2 + 7?',
        'alternativas': {
            

        },
        'resposta_certa': '4'
    },

}

lista_escolhas = ['a', 'b', 'c', 'd']
shuffle(lista_escolhas)
lista_respostas = ['1', '2', '3', '4']

lista = {
    lista_escolhas[0]: '0',
    lista_escolhas[1]: '1',
    lista_escolhas[2]: '2',
    lista_escolhas[3]: '4'
}


for k, v in perguntas.items():
    if v['id'] == 1:
        v['alternativas'] = lista
        print(f'{k} - {v["pergunta"]}')
        for k , v in sorted(lista.items()):
            print(f'{k} - {v}')

        

# def suffle_answers(dictionary: dict, )

