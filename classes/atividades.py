def comer(comida, saudavel):
    if saudavel:
        final = 'quero manter a forma'
    else:
        final = 'a gente só vivi uma vez'

    return f'Estou comendo {comida} porque {final}'


def dormir(horas):
    if horas > 8:
        return f'Putz! Dormi muito! Estou atrasado para o trabalho.'
    else:
        return f'Continuo cansado dormir por {horas} horas.'


def engracada(pessoa):
    comediantes = ['Murilo Couto', 'Ewerton Pereira']
    if pessoa in comediantes:
        return True
    return False

