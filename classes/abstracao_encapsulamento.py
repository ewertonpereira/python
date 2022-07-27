"""
Abstração e Encapsulamento

O grande objetivo da Programação Orientada a Objeto é encapsular nosso código dentro de um grupo lógico
e hierárquico utilizando Classes.

Encapsular -> Cápsula

# Relembrando Atributos/Métodos pricados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atribudo privado chamado __nome e uma método privado 
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas Python não bloqueia 
este acesso fora da classe. Com Python acontece o fenômeno chamado Name Mangling, que faz alteração 
na forma de se acessar os elementos privados, conforme:

    _Classe__elemento

Exemplo - Acesssando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração, em Programação Orientada a Objeto, é o ato de expor apenas dados relevantes de uma classe. 
Escondendo atributos e métodos privados de usuários.

"""
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente!')
        else: 
            print('O valor deve ser positivo')


    def transferir(self, valor, conta_destino):
        # 1 - Remover valor da conta de origem 
        self.__saldo -= valor
        self.__saldo -= 0.10 # Taxa de transferência paga por quem realiziu a transferência
        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor


# Testando

conta1 = Conta('Ewerton', 150, 1500)
conta1.extrato()
conta2 = Conta('Lauren', 2000, 50000)
conta2.extrato()

"""
print(conta1.__dict__)
conta1.extrato()

print(conta1._Conta__titular) # Name Mangling

conta1._Conta__titular = 'Batoré'

print(conta1.__dict__)

conta1.depositar(150)
print(conta1.__dict__)

conta1.sacar(200)
print(conta1.__dict__)
"""
conta2.transferir(100, conta1)
conta1.extrato()
conta2.extrato()

