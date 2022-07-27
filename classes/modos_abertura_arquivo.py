"""
MOdos de abertura de arquivo

r -> Abre para leitura - padrão.
w -> Abre para escrita - sobrescreve cas o arquivo já exista.
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExisteEror.
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e escrita.

# OBS: Abrindo no modo a, que é append, se o arquivo não existir será criado. Caso exista o novo 
conteúdo sempre será adicionado ao final do arquivo. Com o modo 'a', não controlamos o cursor.

http://docs.pytohn.org/3/library/functions.html#open

"""
# Exemplo x

try:
    with open('borabora.txt','x') as arquivo:
        arquivo.write('Teste de conteúdo.\n')
except FileExistsError:
    print('Arquivo já existe!')


with open('fruit.txt', 'a') as file:
    while True:
        fruit = input('Informe o nome da fruta ou digite sair para sair: ')
        if fruit != 'sair':
            file.write(fruit + '\n')
        else:
            break

with open('fruit.txt', 'r+') as file:
    file.seek(0)
    file.write('glu. glu.\n')

