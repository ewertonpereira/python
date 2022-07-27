"""
Loop while

Forma geral

While expressão_booleana:
    //expressão do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde  o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5 (False)

# Exemplo 1

number = 1 

while number < 10:
    print(number)
    number += 1
    
# OBS: em um loop while é importante que cuidemos do critério de parada.
"""
resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jésica? ')
