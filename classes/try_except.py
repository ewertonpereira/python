"""
O bloco try/except para tratar os erros que podem ocorrer no nosso código> previnindo assim que o programa 
para de funcionar e o usuário receba mensagens de erro inesperadas.

A forma  geral mais simples é:

try:
    //EXECUÇÃO PROBLEMÁTICA
except:
    //o que deve ser feito em caso de probema


"""
# Exemplo 1 - Tratando um erro genérico

try:
    geek() # Problema tratado
except:
    print('Deu schaboo!!!')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

# OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é sempre 
# tratar de forma específica.

# Exemplo 2 - Tratando um erro específico

try:
    geek()
except NameError as err: # Nomeando e mostrando o erro
    print(f'A aplicação gerou o seguinte erro: {err}')


try:
    #len(5)
    #geek()
    print('geek'[9])
except NameError as err:
    print(f'Deu NameError: {err}')
except TypeError as err2:
    print(f'Deu NameError: {err2}')
except:
    print('Deu um erro diferente!')


def pega_valor(dic, chave):
    try:
        return dic[chave]
    except KeyError:
        return None


dic = {'nome': 'Ewerton'}

print(pega_valor(dic, 'zé'))
