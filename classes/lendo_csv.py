"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

http://dados.gov.br/dataset

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:

    - reader -> Permite que iteremos sobre as listas do arquivo CSV comos listas
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts


"""
# Possível de se trabalhar, mas não é ideal (trabalhoso)

with open('lutadores.csv', encoding='utf8') as file:
    data = file.read()
    #print(type(data))
    data = data.split(',')[2:]
    print(data)

print('-------------------------------------------')
# Reader

from csv import reader

with open('lutadores.csv', encoding='utf8') as file:
    data = reader(file)
    next(data) # Pular o cabeçalho
    for linha in data:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no país {linha[1]} e mede {linha[2]} centímetros')


print('-------------------------------------------')
from csv import DictReader

with open('lutadores.csv', encoding='utf8') as file:
    data = DictReader(file) #  data = DictReader(file, delimiter='')  Define delimitador
    for linha in data:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no país {linha['País']} e mede {'Altura (em cm)'} centímetros")

    
    