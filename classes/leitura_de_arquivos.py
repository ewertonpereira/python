"""
Leitura de arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente
significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas uma parâmetro de entrada, que nesse 
caso é o nome do arquivo a ser lido. Essa função retorna um _io.TextIOWaper e é com ele que trabalhamos.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão a função opne() abre o arquivo para leitura. Este arquivo deve existir, ou então 
teremos o erro FileNotFoundError.


"""
# Exemplo

arquivo = open('texto.txt')

#print(arquivo)
#print(type(arquivo))

# Para ler o conteúdo de um arquivo, após suas abertura, devemos utilizar a função read()

print(arquivo.read())

# OBS: O Python utiliza um recurso para trabalhar com arquivos chamad cursor.
# Esse cursor funciona como o cursor quando estamos escrevendo.

# OBS: A função read() lê todo o conteúdo do arquivo.
