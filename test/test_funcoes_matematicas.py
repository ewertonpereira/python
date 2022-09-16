"""
    - criar a classe funções matemáticas ok
    - criar o método somar_dois_numeros, sendo esses dois números passados como parâmetros
    - passar dois números como parâmetro
    - testar resultado da função
"""
# def setup_module(modulo):
#     print('\nIniciando  o módulo', modulo.__name__)


# def teardown_module(modulo):
#     print('\nFinalizando  o módulo', modulo.__name__)


# def setup_function(funcao):
#     print('\nIniciando  a função', funcao.__name__)


# def teardown_function(funcao):
#     print('\nFinalizando  a função', funcao.__name__)


# def test_instanciar_funcoes_matematicas():
#     FuncoesMatematicas()

from test.funcoes_matematicas import FuncoesMatematicas


def test_executar_metedo_somar_dois_numeros():
    funcoes = FuncoesMatematicas()
    funcoes.somar_dois_numeros(1, 2)


def test_somar_um_mais_dois_no_metodo_somar_dois_numeros_e_retornar_tres():
    funcoes = FuncoesMatematicas()
    assert funcoes.somar_dois_numeros(1, 2) == 3
    