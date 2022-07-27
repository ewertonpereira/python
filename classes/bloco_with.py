"""
Bloco with

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados
após o bloco with.


"""
# O bloco with - Forma Pytônica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())


# print(arquivo.read()) # Error, o arquivo é fechado após o bloco with
