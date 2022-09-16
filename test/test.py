from datetime import datetime
from time import process_time


# file = open(address, mood)
# with  open('oi.txt', 'r', encoding='utf-8') as file: 
#     content = file.read()
#     print(content)


with open('log.txt', 'w', encoding='utf-8') as file:
    file.write('Horários de log dos funcionários')


# with open('log.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)
status = False
tempo_trabalhado = 0

answer = input('Quer entrar no sistema? ').lower()

if answer == 'sim':
    status = True
    t1 = process_time()
    name = input('Digite seu nome: ').upper()
    with open('log.txt', 'a', encoding='utf-8') as file:
        date_now = datetime.now()
        log = date_now.strftime('%d-%m-%Y %H:%M:%S')
        file.write(f'\n{name} entrou {log}')


if status:
    answer = input('Quer sair do sistema? ').lower()
    if answer == 'sim':
        status = False
        t2 = process_time()
        tempo_trabalhado += (t2-t1)
        with open('log.txt', 'a', encoding='utf-8') as file:
            date_now = datetime.now()
            log = date_now.strftime('%d-%m-%Y %H:%M:%S')
            file.write(f'\n{name} saiu {log}')


with open('log.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)


print(tempo_trabalhado) 