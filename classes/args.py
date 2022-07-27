"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Ossi significa que você poderá chamar de qualquer coisa,
desde que começe com *.

Exemplo:

*Xis

mas por convensão, utilizamos *args para definí-lo

Mas o que  é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
Então desde já lembre-se que tuplas são imutáveis.


# Exemplos

def soma_todos_numeros(num1=1, num2=2, num3=3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 3, 5))

#print(soma_todos_numeros(4, 3)) 
#print(soma_todos_numeros(4, 3, 5, 8)) # Type error

# Entendendo o args

def soma_todos_numeros(*args):
    return sum(args) 

print(soma_todos_numeros(4))
print(soma_todos_numeros(4, 3))
print(soma_todos_numeros(4, 3, 5))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo!'
    return 'Eu não tenho certeza quem você é...'


print(verifica_info()) # Eu não tenho certeza quem você é...
print(verifica_info(1, True, 'University', 'Geek')) # Bem-vindo!
print(verifica_info(1, 'University', 3.145)) # Eu não tenho certeza quem você é...

"""
def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

print(soma_todos_numeros(*numeros)) 

""" 
O * serve para que informemos ao Python que estamos passando como argumento uma coleção de daddos, 
desta forma, ele saberá que precisará antse desempacptas esses dados.
"""
