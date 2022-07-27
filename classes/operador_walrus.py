"""
Operador Walrus - > Permite fazer a atribuição e retorno de valor em uma única expressão.

variável := expressão
"""
nome: str = 'Ewerton'
print(nome)

print(nome := 'Bruninha')

# Python 3.7

cesta = []
fruta = input('Inoforme a fruta: ')
while fruta != 'sair':
    cesta.append(fruta)
    fruta = input('Inoforme a fruta: ')


print(cesta)

# Python 3.8

cesta = []
while (fruta := input('Inoforme a fruta: ').title()) != 'Sair':
    cesta.append(fruta)


print(cesta)
