"""
JSON e Pickle

JSON -> JAvaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas(Twitter, Facebook, Youtube...)
e terceiros (nós desenvolvedores).

ret = json.dumps(['produto', {'ps4': ('2TB', 'Novo', '220V', 25644)}])

print(type(ret))
print(ret)

Integrando o JSON com o Pickle
"""
# Escrevendo arquivo json/pickcle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

    
jarbas = Gato('Jarbas', 'RND')

#print(jarbas.__dict__)
#ret = json.dumps(jarbas.__dict__)
#ret = jsonpickle.encode(jarbas)
#print(ret)
"""
with open('jarbas.json', 'w') as file:
    ret = jsonpickle.encode(jarbas)
    file.write(ret)
"""

# Lendo arquivo json/pickcle

with open('jarbas.json', 'r') as file:
    conteudo = file.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)

