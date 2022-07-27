"""
Debuggando com PDB

PDB -> Pytohn Debbugger


"""

# OBS: A utilização do print() para debuggar o código é uma prática ruim

def dividir_hard(a, b):
    try:
        return int(a) / int(b)
    except ValueError as errone:
        return (f'Valor incorreto! {errone}')
    except ZeroDivisionError as errtwo:
        return (f'Não é possível realizar uma divisão por 0. ERRO: {errtwo}')

print(dividir_hard(4, 0))

"""
Existem formas mais profissioonais de fazer esse 'debug', utilando o  debbugger

Em Python, podemos fazer isso em diferentes IDEs, como o Pycharm ou utilizando o PDB - Python Debugger


# Exemplo com PDB - Python Debugger

Para utilizar o Python Debugger precisamos** importar a biblioteca pdb e então utilizar a função set_trace()

** A partir do  Python 3.7 não é mais necessário importar a biblioteca pdb, pois o comando do debug foi
incorporado  como função bult-in(integrada) chamada breakpoint()

Comandos básicos do PDB

    l -> Listar onde estamos no código
    n -> Próxima linha
    p -> Imprime variável
    c -> continua execução - finaliza o debugger

"""
import pdb

nome = 'Ewerton'
sobrenome = 'Pereira'
#breakpoint()
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Python is life'
final = nome_completo + ' ' + curso
print(final)

# import pdb; pdb.set_trace()

"""
# Por quê utilizar este formato?

O debug é utilizado durante o desenvolvimento. Costumamos realizar  todos os importes de bibliotecas
no início do arquivo. \Por isso, ao invés de colocarmos o import  do pdb no início do arquivo, 
nós colocamos somente onde vamos debuggar, e ao finalizarmos já podemos fazer a remoção.

# OBS: Cuidado com os conflitos entre nomes de variáveis e os comandos do pdb

Como os nomes da variáveis podem ser iguais aos comandos do pdb, devemos utilizar p para imprimir  o valor da 
variável. Ou seja: p nome_variavel
"""
