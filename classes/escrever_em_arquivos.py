"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura não podemos realizar a escrita nele. Apenas ler. Da mesma forma 
se abrirmos um arquivo para escrita não podemos lê-lo, sómente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrever dados em um arquivo, após abrir o arquivo utilizamos a função write().

Essa função recebe uma string como parâmetro, caso contrario teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado, caso ele já exista,
o anterior será apagado e  um novo arquivo será criado. Dessa forma, todo o conteúdo no arquivo anterior
é perdido.
"""
# Exemplo de escrita - modo 'w' - write

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos é muito fácil.\n')
    arquivo.write('Podemos escrever muitas linhas.\n')
    arquivo.write('Arêrêêe! O Grêmio vai jogar a série B!!!')


with open('novo.txt') as arquivo:
    print( arquivo.read())


with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break


with open('frutas.txt') as arquivo:
    print( arquivo.read())
