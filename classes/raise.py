"""
Levanando os próprios erros com raise

raise -> Lança exceções 

OBS: raise não é uma função. É uma palavra reservada, assim como def ou qualquer outa em Python

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens
de erro.

A forma geral de utilização é: 

raise TipoDeErro('Mensagem de erro')


"""
# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Texto precisa ser uma string')
    
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Ewerton Pereira', 'Vermelho')
#colore(9, 00) # Mostra a definição de erro que colocamos em raise

def colore20(texto, cor):

    cores = ('Verde', 'Amarelo', 'Vermelho', 'Azul')

    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')

    if type(cor) is not str:
        raise TypeError('Texto precisa ser uma string')

    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')

    print(f'O texto {texto} será impresso na cor {cor}')


colore20('Ewerton Pereira', 'Preto')

# OBS: O raise, assim como return, finaliza a função. Ou seja, nada após o raise é executado.
