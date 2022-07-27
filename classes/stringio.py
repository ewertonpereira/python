"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistemas operacional o software precisa ter permissão:
   
    - Permissão de leitura -> Para ler o arquivo;
    - Permissão de escrita -> Para escrever o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória.
"""
# Primeiro fazemos o import

from email import message
from io import StringIO
import string

message = 'Está é apenas uma string normal.'

# Podemos criar um aarquivo em memória já com uma string inserida ou mesmo vázio para inserirmis um texto depois

file = StringIO(message)

# file = open('file.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos

print(file.read())

file.write('\nOutro texto')

# Podemos inclusive movimentar o cursor
file.seek(0)
print(file.read())
