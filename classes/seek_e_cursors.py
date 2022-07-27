"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe uma parâmetro que
indica onde queremos colocar o cursor
"""
arquivo = open('texto.txt')
print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()

arquivo.seek(0) # seek
print(arquivo.read())

# readline() -> Função que lê o arquivo linha por linha

arquivo = open('texto.txt')
print(arquivo.readline())

arquivo = open('texto.txt')

# readlines() faz uma lista com cada linha

print(arquivo.readlines())

# Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo do disco do computador
# com o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo
# fechar essa coneção. Para isso utilizamos a função close().

arquivo = open('texto.txt')
print(arquivo.read())
print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado
arquivo.close()

arquivo = open('texto.txt')
print(arquivo.read(12)) # Limita o número de caracteres
arquivo.close()

