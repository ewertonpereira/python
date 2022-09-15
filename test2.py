"""
    - se a função somar_dois_numeros existe
    - passar dois números como parâmetro
    - testar resultado da função
"""
def test_soma_da_funcao_somar_dois_numemros():
    assert somar_dois_numeros(1, 2) == 3


def somar_dois_numeros(num1, num2):
    return num1 + num2