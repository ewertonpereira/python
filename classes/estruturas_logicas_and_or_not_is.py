"""
Estruturas lóginas: and, or, not e is

Operadores unários:
    - Not.
    
Operadores binários:
    -And, or, is.
    
### Regras de funcionamento:
    
Para o 'and' ambos os valores precisam ser True.

Para o 'or' um ou outro valor precisa ser True.

para o 'not' o valor do booleano é invertido, ou seja se for True vira False e vice-versa.

Para o 'is' o valor é comparado com um segundo.

"""
ativo = False
logado = True

if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar a sua conta, Favor, verifique seu e-mail.')

if not ativo:
    print('Você precisa ativar sua conta')
else:
    print('Bem-vindo usuário')
    
#Exemplo contrário 
print(not True)
print(not False)

"""
ex: 

if ativo is True: // is ativo true? R: True
    print('Bem-vindo usuário')
    
"""
