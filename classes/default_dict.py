"""
Módulo Collections - Defual Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap dicionários

dic = {'curso': 'Python'}
print(dic)
print(dic['curso'])
print(dic['outro']) # Error

Default Dict -> Ao criarmos um dicionário utulizando-o nós informamos um valor default, podendo utilizar
um lambda para isso. Esse valor seráutilizado sempre que não ouver um valor definido. Caso tentamos acessar 
uma chave que não existe, essa será criada e o valor default será atribuído.

OBS: Lambdas são funções sem nomes, que podem ou não receber parâmetros de entrada e retornar valores.
"""
from collections import defaultdict

dic = defaultdict(lambda: 0)

dic['Curso'] = 'Python'
print(dic)
print(dic['outro'])
print(dic)
