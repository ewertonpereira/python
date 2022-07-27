"""
Sistemas de arquivos - Manipulação


"""
import os

# Descobrindo se um arquivo ou diretório existe

print(os.path.exists('fruit.txt')) # True
print(os.path.exists('file.txt')) # False
print(os.path.exists('classes')) # False

# Criando arquivos

# Forma 1

open('arquivo-teste.txt','w').close()

# Forma 2

open('arquivo-teste2.txt','a').close()

# Forma 3

with open('arquivo-teste3.txt','w') as file:
    pass


# Forma 4

# os.mknod('arquivo-teste4.txt')

# Criando diretório

# os.mkdir('templates', exist_ok=True) #  exist_ok=True -> Se diretório já existir, ignora

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos um FileExistError

# Criando multiplos diretórios

os.makedirs('templates/dir1/dir2', exist_ok=True)

# Renomear arquivos e diretórios

os.rename('templates', 'templatesssss', exist_ok=True)

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Removendo arquivos

# ATENÇÂO: Tome cuidado com os camandos de deleção. Ao deletarmos um arquivo ou diretório eles não vão para a lixeira, eles somem.

os.remove('arquivo-teste3.txt')

# OBS: Se você estiver no Windowns e o arquivo que você quer deletar estiver em uso, você terá um erro.

# OBS: Caso o arquivo não exista, teremos FileFoundError

# OBS: Se você informar um diretório ao invéns de um arquivo, teremos um IsADirectoryError

# Removendo diretórios

os.rmdir('templatesssss')

# Removendo árvore de diretórios

for aquivo in os.scandir('templates'):
    if aquivo.is_file():
        os.remove(aquivo.path)