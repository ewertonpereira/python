"""
Assertions

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes.

Utilizamos o assert em uma expressão que queremos chegar se é valida ou não.
Se a expressão for verdadeira, retorna NOne e caso seja falsa levanta um erro do tipo AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada.

# OBS : A palavra assert pode ser utilizada em qualquer função ou código nosso... não precisa ser exclusivamente nos testes.

# ALERTA: Cuidado ao utilizar 'assert'

Se um program Python for executado com o parâmetro -O, n enhum assertion será validado. Ou seja todas as 
suas validações já eram.


"""
def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos!'
    return a + b


# ret = soma_numeros_positivos(-2, 4) # AssertionError
#print(ret)

def comer_fastfood(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')
print(comer_fastfood(comida))
