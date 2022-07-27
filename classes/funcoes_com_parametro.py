"""
Funções com Parâmetros(de entrada)

Funções que recebem dados para serem processados dentro da mesma.

Se a gente pensar  em um programa qualquer, geralmente temos: 
    - Entrada;
    - Processamento;
    - Saída.
    
Se pensarmos em uma função, já sabemos que temos funções que:
    - Não possuem entrada;
    - Não possuem saída;
    - Possiem entrada, mas não possuem saída;
    - Não possuem entrada, mas possuem saída,
    - Possuem entrada e saída.
    
# Exemplo função

num = int(input('Digite um número inteiro: '))
 
def square(number):
    return number ** 2


print(square(num))

# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada em uma função quantos 
parâmetros forem necessários. Eles são separados por vírgula.

 # Exemplo 

def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def outra(n, b, m):
    return (n + b) * m


print(soma(2, 5))
print(multiplica(9,2))
print(outra(3, 2, 'Oi '))

# OBS: Se a gente informar um número errado de parâmetro ou argumento, teremos TypeError

# Nomeando parâmetros

def nome_completo(name, lastName):
    return f'Seu nome completo é {name} {lastName}'


print(nome_completo('Ewerton', 'Pereira'))

# Diferênça entre parâmetro e argumento

Parâmetros são variáveis declaradas na definição da uma função.
Argumentos são dados passados durante a execução de uma função.

# A ordem os parâmetros importa!

# Argumentos nomeados(KeyWord Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos usar qualquer ordem.
name = 'Bolinha'
lastName = 'Amarela'

print(nome_completo(name=name, lastName=lastName))
print(nome_completo(lastName='Silva', name='Godofredo'))

""" 
# Erro comum na utilização de return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total # Colocar o return no lugar certo


lista = list(range(1,10))
print(lista)
print(soma_impares(lista))
