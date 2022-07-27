"""
Argumentos somente posicionais
"""
def cumprimenta_v1(nome):
    return f'Olá {nome}'


print(cumprimenta_v1('fela da poota'))
print(cumprimenta_v1(nome='ewertonzinho'))

def cumprimenta_v2(nome, /):
    return f'Olá {nome}'


print(cumprimenta_v2('fela da poota'))
#print(cumprimenta_v2(nome='ewerton')) # TypeError: cumprimenta_v2() got some positional-only arguments passed as keyword arguments: 'nome'

def cumprimenta_v3(nome, /, mensagem='Bom dia'):
    return f'{mensagem} {nome}'


print(cumprimenta_v3('Maricota'))
print(cumprimenta_v3('Jordan', mensagem="Vai tomar no butico"))
print(cumprimenta_v3('Muri-Muri', 'Me gusta'))

def cumprimenta_v4(*, nome): # Nome obrigatório
    return f'Olá {nome}'


print(cumprimenta_v4(nome='Ewerton'))
#print(cumprimenta_v4('Ewerton'))
