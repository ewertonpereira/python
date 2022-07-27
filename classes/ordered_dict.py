"""
Módulo Collect - Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict

OrderDict é um dicionário que nos garante a ordem de inserção dos elementos.

from collections import OrderedDict

d = OrderedDict({'a': 1, 'b': 5, 'c': 3, 'd': 4})

for chave, valor in d.items():
    print(f'Chave: {chave}   Valor: {valor}')
    

"""
# Import

from collections import OrderedDict

# Entendendo a diferença entre Dict e orderedDict

# Dicionários comuns

dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 2, 'a': 1}
print(dic1 == dic2) # True -> Já que a ordem ods elementos não importa para o dicionário

# OrderedDict

odic1 = OrderedDict({'a': 1, 'b': 2})
odic2 = OrderedDict({'b': 2, 'a': 1})
print(odic1 == odic2) # False -> Já que a ordem os elementos importa para o orderedDict

