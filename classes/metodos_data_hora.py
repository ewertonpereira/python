"""
Métodos de data e hora
"""
import datetime
from xmlrpc.client import DateTime
from textblob import TextBlob

# Com now podemos especificar um timezone (fuso horário)
agora = datetime.datetime.now()
print(agora)

hoje = datetime.datetime.today()
print(hoje)

# Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)

# Encontrar o dia da semana. weekday()

# OS dias da semana do método weekday() começam em 0, sendo esta a segunda-feira
"""
0 - Monday
1 - Tuesday
2 - Wednesday
3 - Thursday
4 - Friday
5 - Saturday
6 - Sunday


print(manutencao.weekday())

aniversario = input('Qual a sua data de nascimento(dd/mm/yyyy): ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print(f'Você nasceu em uma segunda-feira!')
elif aniversario.weekday() == 1:
    print(f'Você nasceu em uma terça-feira!')
elif aniversario.weekday() == 2:
    print(f'Você nasceu em uma quarta-feira!')
elif aniversario.weekday() == 3:
    print(f'Você nasceu em uma quinta-feira!')
elif aniversario.weekday() == 4:
    print(f'Você nasceu em uma sexta-feira!')
elif aniversario.weekday() == 5:
    print(f'Você nasceu em um sábado!')
elif aniversario.weekday() == 6:
    print(f'Você nasceu em uma domingo!')
"""
def date_format2_0(date):
    return f"{date.day} de {TextBlob(date.strftime('%B')).translate(to='pt-br').title()} de {date.year}"
    

def date_format(date):
    if date.month == 1:
        return f'{date.day} de Janeiro de {date.year}'
    elif date.month == 2:
        return f'{date.day} de Fevereiro de {date.year}'
    elif date.month == 3:
        return f'{date.day} de Março de {date.year}'
    elif date.month == 4:
        return f'{date.day} de Abril de {date.year}'
    elif date.month == 5:
        return f'{date.day} de Maio de {date.year}'
    elif date.month == 6:
        return f'{date.day} de Junho de {date.year}'
    elif date.month == 7:
        return f'{date.day} de Julho de {date.year}'
    elif date.month == 8:
        return f'{date.day} de Agosto de {date.year}'
    elif date.month == 9:
        return f'{date.day} de Setembro de {date.year}'
    elif date.month == 10:
        return f'{date.day} de Outubro de {date.year}'
    elif date.month == 11:
        return f'{date.day} de Novembro de {date.year}'
    elif date.month == 12:
        return f'{date.day} de Dezembro de {date.year}'


# Formatando datas/horas com strtime() - String Format Time

hoje_formatado = hoje.strftime('%d de %B de %Y') # y = 00 | Y = 0000  | B Nome do mês completo | b Nome do mês iniciais
print(hoje)
print(hoje_formatado)

print(date_format(hoje))
print(date_format2_0(hoje))

#nascimento = input('Qual a sua data de nascimento(dd/mm/yyyy): ')
#nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
#print(nascimento)

almoco = datetime.time(12, 30, 0)
print(almoco)

# Marcando tempo de execução do nosso código com timeit

import timeit, functools

# Loop for

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
print(tempo)

# List Comphension 

tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=1000)
print(tempo)

# Map

tempo = timeit.timeit('"-".join(map(str, range(100)))', number=1000)
print(tempo)

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma += + num ** num + 4
    return soma 


print(timeit.timeit(functools.partial(teste, 2), number=10000))
