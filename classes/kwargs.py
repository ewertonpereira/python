"""
**Kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, 
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros e um dicionário.

# Exemplo

def cores_favoritas(**kwargs):
    for pessoa,cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}') # Tille

cores_favoritas(marco='verde', ewerton='vermelho', gabi='preto')

# OBS: Nem os parâmetros *args e **kwargs não são obrigatórios

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs ['geek'] == 'Python':
        return 'Você recebeu um comprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções, podemos ter (NESTA ORDEM):

Parâmetros obrigatórios;
    - *args
Parâmetros default (não obrigatório);
    - **kwargs


"""
def minha_funcao(nome, idade,  *args, solteiro=False, **kwargs):
    print (f'{nome.title()} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao('julia', 8)
minha_funcao('ewerton', 18, 4, 5, 6, solteiro=True)
minha_funcao('gabi', 17, eu='Não', voce='Vai')
minha_funcao('tobias', 27, 9, 3, 7, java=False, python=True)

print('------------------------------')

# Função com a ordem incorreta de paraâmetros

#def mostra_info(a, b, instrutor='Geek', *args,  **kwargs):
    #return [a, b, args, instrutor, kwargs]

"""
a = 1
b = 2
args = ()
instrutor = 3
kwargs = {'sobrenome': 'University', 'cargo': 'instrutor'}
"""

# Função com a ordem certa de parâmetros

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

"""
a = 1
b = 2
args = (3)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'instrutor'}
"""

# Entenda por quê é importante manter a ordem dos parâmetros na declaração

print(mostra_info(1, 2, 3, sobrenome='University', cargo='instrutor'))

print('------------------------------')

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': "Ewerton", 'sobrenome': 'Pereira'}

print(mostra_nomes(**nomes))
print('------------------------------')

def soma_multiplos(a, b, c):
    print (a + b +c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)

soma_multiplos(*lista)
soma_multiplos(*tupla)
soma_multiplos(*conjunto)
soma_multiplos(**dicionario)

# OBS: Os nomes da chave em um dicionário devem ser os mesmos dos nomes dos parâmetros da função

#dicionario = dict(a=1, b=2, c=3)
#soma_multiplos(**dicionario) # TypeError 

# soma_multiplos(**dicionario, lang='Python') # Funciona com ** kwargs na função, se não da erro 
