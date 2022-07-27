"""
Escrevendo em arquivos CSV

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista. 
"""

from csv import writer

with open('filmes.csv', 'w') as file:
    escritor = writer(file)
    filme = None
    escritor.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme em minutos: ')
            escritor.writerow([filme, genero, duracao])

            
# DictWriter

# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.

from csv import DictWriter

with open('filmes.csv', 'w') as file: # a serve para add algo no arquivo
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor = DictWriter(file, fieldnames=cabecalho)
    escritor.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme em minutos: ')
            escritor.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})


