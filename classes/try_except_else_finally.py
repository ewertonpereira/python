"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA E DADOS DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.


"""
# Else -> É executado somente se não acontecer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou: {num}')


# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou: {num}')
finally:
    print('Executando o finally')


# OBS: O bloco finally é sempre executado. Independente se ouve exceção ou não.

# O finally gerealmente é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b

try:
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')
else:
    print(dividir(num1,num2))

# Exemplo mais complexo CORRETO

# OBS: VOCÊ É RESPONSÁVEL PELAS ENTRADAS DAS SUAS FUNÇÕES. ENTÃO, TRATE-AS!!!

def dividir_hard(a, b):
    try:
        return int(a) / int(b)
    except ValueError as errone:
        return (f'Valor incorreto! {errone}')
    except ZeroDivisionError as errtwo:
        return (f'Não é possível realizar uma divisão por 0. ERRO: {errtwo}')


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir_hard(num1, num2))
