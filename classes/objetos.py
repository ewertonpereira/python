"""
Objetos

Objetos -> São instâncias da classe, ou seja, após o mapeamento do objeto do mundo real para sua repersentação 
computacional, devemos podemos poder criar quantos objetos forem necessários. Podemos nos objetos/instâncias 
de uma classe como variáveis do tipo na classe. 
"""
from ast import USub


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz oi!')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instânca/Objeto
lamp1 = Lampada('branca', 110, 60)

lamp1.ligar_desligar()

print(f'A Lâmpada está ligada? {lamp1.checa_lampada()}')

user1 = Usuario('Ewerton', 'Pereira', 'ewerton854850458049@bol.com.br', '123456')

cli1 = Cliente('jarbas', '12345678921')

cc = ContaCorrente(3000, 10000, cli1)

cc.mostra_cliente()
cc._ContaCorrente__cliente.diz() # ACESSO DE FORMA ERRADA
