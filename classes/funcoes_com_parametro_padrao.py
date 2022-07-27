"""
Funções com Parâmetro Padrão (Default Parameters)

Funções onde a passagem de parâmetro seja opcional.

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Ewerton')
print()

# Exemplo de função onde a passagem de parâmetro seja obrigartório

def square(number):
    return number ** 2
    
print(number(3))
print(number()) # Error


def exponencial(numero, potencia=2): # Por padrão eleva ao quadrado 
    return numero ** potencia


print(exponencial(3)) # Por padrão eleva ao quadrado 
print(exponencial(2,3)) # Eleva a potência informada pelo usuário

#OBS: Se o usuário passar somente um argumento, este será atriuído ao primeiro número e será 
calculado  deste número.

#OBS: Em funções Python, os parâmetros com valores default(padrão) DEVEM sempre estar ao final na declaração


# Exemplo 

def mostra(nome='Ewerton', instrutor=False):
    if nome =='Ewerton' and instrutor:
        return 'Bem-vindo instrutor Ewerton'
    elif nome == 'Ewerton':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra())
print(mostra(instrutor=True))
print(mostra(True))
print(mostra('Ewerton'))
print(mostra(nome='Jorgino'))

Por quê utilizar parâmetros com valor default?
    - Nos permite ser mais flexível nas funções;
    - Evita erros com parâmetros incorretos;
    - Nos permite trabalhar com exemplos mais legíveis de código.
    
# Exemplo LEGAL

def soma(n1, n2):
    return n1 + n2


def mat(n1, n2, fun=soma):
    return fun(n1, n2)


def subtracao(n1, n2):
    return n1 - n2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões

Variáveis globais
Variáveis locais

OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência

# Atenção com variáveis globais(sempre tentar evitar)

"""
from typing import Container


total = 0

def incrementa():
    global total # Avisando que queremos utilizar a variável global
    total +=1
    return total


print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador # Utilizar variável como não local
        contador += 1
        return contador
    return dentro()


print(fora)
