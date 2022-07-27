"""
Métodos

Métodos(Funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em dois grupos: Métodos de instância e Médodos de Classe.

# O método dunder init __init__ é um método especial chamado de construtor e sua função é construir
o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS : Os métodos Dunder em Python são chamados de métodos mágicos.

ATENÇÃO: Por mais que possamos criar nossas próprias funções utilizando Dunder, não é aconselhado. Python possui varios métodos 
com esta forma de nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas internas da linguagem.
Então evite ao máximo. De preferência nunca o faça.

# OBS: Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas 
por underline.

# Métodos de Classe em Python são conhecidos como Métodos estáticos em outras linguagens.
"""
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor 
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """[Summary]

        Args:
            porcentagem ([int]): [Retorna o valor do produto com desconto]
        """
        return (self.__valor * (100 - porcentagem)) / 100


# from passlib.hash import pbkd_sha256 as cryp

class Usuario:

    contador = 0
    
    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuários no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome,  email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
#       self.__senha = cryp.hash(senha, rounds=2000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


    def __gera_usuario(self):
        return self.__email.split('@')[0]

"""
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
"""
            
p1 = Produto('Bala de goma', 'Doce', 200)
print(p1.desconto(10))
print(Produto.desconto(p1, 40)) # self, desconto

user1 = Usuario('Ewerton', 'Pereira', 'ewerton@bol.com', '123456')
user2 = Usuario('Lauren', 'Pereira', 'lauren_gatinha99', 'ewertongostoso')

print(user1.nome_completo())
print(user2.nome_completo())
# print(f'Senha User1: {user1._Usuario__senha}') # Acesso  de forma errada de um atributo de classe
# print(f'Senha User2: {user2._Usuario__senha}') # Acesso  de forma errada de um atributo de classe

# Métodos de Classe

user3 = Usuario('jarbas', 'Foda','jarbinhas@bol.com.br', '123456')

Usuario.conta_usuarios() # Forma correta
user3.conta_usuarios() # Possível, mas incorreta

user4 = Usuario('McGaiver', 'Da Musta', 'magaivinho@outlook.com', '1234')

print(user4._Usuario__gera_usuario()) # Acesso, de forma ruim...

# Método Estático

print(Usuario.contador)
print(Usuario.definicao())

print(user3.contador)
print(user3.definicao())
