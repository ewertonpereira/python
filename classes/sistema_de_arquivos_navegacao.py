"""
Sistemas de arquivo e navegação

Para fazer uso de manipulação de arquivos do sistema operaconal, precisamos importaar e fazer uso do 
módulo os.

os -> Operating System
"""
import os
import sys

# getcwd() -> Pega ocurrent work directory - Retorna o path absoluto

print('After this!')
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..') # Volta um diretório
print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo

# Para usuário linux
# print(os.path.isabs('/home/nome_diretório')) # Linux

# Para usuário windowns
print(os.path.isabs('C:\\Users\\Ewerton\\Desktop\\Projetos')) # Windowns

# Podemos identificar o sistema operacional com o módulo os

print(os.name) # posix (linux e Mac), nt (Windowns)

# Podemos ter mais detalhes no sistema operacional

# print(os.uname()) # Linux

print(sys.platform)

print(os.getcwd()) # C:\Users\Ewerton\Desktop

#res = os.path.join(os.getcwd(),'nome do arquivo')

#os.chdir(res)
#print(os.getcwd())


# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o diretório
# que será juntado ao atual.

# Podemos listar os arquivos e diretórios com o listdir()

print(len(os.listdir())) # Quantidad de arquivos

print(os.listdir('C:\\'))

# Podemos listar os arquivos e diretórios mais detalhes com o scandir()

print(list(os.scandir('C:\\')))

# OBS: Quando utilizamos a função sacndir() nós precisamos fecha-lá, assim 
# como quando aabrimos um arquivo

