"""
Manipulando data e hora

Python tem um módulo bilt-in para se trabalhar com data e hora chamado datetime.
"""
import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print(datetime.datetime.now()) # 2022-02-13 19:12:03.054718

# datetime.datetime(year, month, day, minute, second, microsecond)
print(repr(datetime.datetime.now()))
print('----------------------------')

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()
print(inicio)

# Altera o horário para 16h, o min, 0 seg, 0 microseg

inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

print('----------------------------')

evento = datetime.datetime(2023, 1, 1, 0)
print(type(evento))
print(evento)

# Recebendo dados do usuário e convertendo data Python

nascimento = input('Informe sua data de nascimento(dd/mm/yyyy): ')

nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))
print('----------------------------')

# Acessa individual dos elementos de data e hora

print(evento.year) # Ano
print(evento.month) # Mês
print(evento.day) # Dia
print(evento.hour) # Hora
print(evento.minute) # Minuto
print(evento.second) # Segundo
print(evento.microsecond) # Microsegundo
