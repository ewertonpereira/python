questions: dict = {
    '01': {
        'question': 'Quanto é 2 + 2?',
        'answers': {
            'a': '5',
            'b': '3',
            'c': '4',
            'd': '63'
        }, 
        'corect_answer': 'c'
    },
    '02': {
        'question': 'Quem descobriu a américa?',
        'answers': {
            'a': 'Pedro Álvares Cabral',
            'b': 'Dom Pedro I',
            'c': 'Cristóvão Colombo',
            'd': 'Bartolomeu Dias'
        }, 
        'corect_answer': 'a'
    },
    '03': {
        'question': 'Qual o nome da galáxia em que está o sistema solar?',
        'answers': {
            'a': 'Redemoinho',
            'b': 'Sombreiro',
            'c': 'Andrômeda',
            'd': 'Via Láctea'
        }, 
        'corect_answer': 'd'
    },
    '04': {
        'question': 'Quem é o lateral direito titular do Brasil na copa do mundo 2002?',
        'answers': {
            'a': 'Belleti',
            'b': 'Maicon',
            'c': 'Cafu',
            'd': 'Daniel Alves'
        }, 
        'corect_answer': 'c'
    },
    '05': {
        'question': 'Quanto é 3 + 5 * 2?',
        'answers': {
            'a': '13',
            'b': '10',
            'c': '16',
            'd': '17'
        }, 
        'corect_answer': 'a'
    },
    '06': {
        'question': 'O tomate é?',
        'answers': {
            'a': 'Uma leguminosa ',
            'b': 'Uma fruta',
            'c': 'Um tubérculo',
            'd': 'Um vegetal'
        }, 
        'corect_answer': 'b'
    },
    '07': {
        'question': 'Qual desses animais não é um mamífero?',
        'answers': {
            'a': 'Tubarão',
            'b': 'Ornitorrinco',
            'c': 'Tamanduá',
            'd': 'Hipopótamo'
        }, 
        'corect_answer': 'a'
    },
    '08': {
        'question': 'Quantos olhos tem um ciclope na mitologia grega?',
        'answers': {
            'a': '4',
            'b': '3',
            'c': '2',
            'd': '1'
        }, 
        'corect_answer': 'd'
    },
    '09': {
        'question': 'Quantos estados possui a regição sul do Brasil?',
        'answers': {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4'
        }, 
        'corect_answer': 'c'
    },
    '10': {
        'question': 'As _______ são responsáveis pela produção de energia para todo o orgânismo.',
        'answers': {
            'a': 'Organélas',
            'b': 'Mitocôndrias',
            'c': 'Bactérias',
            'd': 'Companias elétricas'
        }, 
        'corect_answer': 'b'
    },
}

# show questions and answers
for question_key, question_value in questions.items():
    print(f'{question_key} - {question_value["question"]}')
   
    for answer_key, answer_value in question_value['answers'].items():
        print(f'{answer_key} - {answer_value}')