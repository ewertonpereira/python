"""
Propriedades - Properties

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes, costumamos 
criar métodos públicos para manipulação desses atributos. Esses métodos são conhecidos por getters e 
setters, onde getters retornam o valor do atibuto e os setters alteram o valor do mesmo.
"""
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente: {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular): ##################
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    
cont1  = Conta('Ewerton', 500, 1500)
cont2  = Conta('Josebar', 5000, 15000)

print(cont1.extrato())
print(cont2.extrato())

#soma = cont1._Conta__saldo + cont2._Conta__saldo
soma = cont1.get_saldo() + cont2.get_saldo()
print(f'A soma do saldo das contas é: {soma}')

print(cont1.__dict__)
cont1.set_titular('Durval')
print(cont1.__dict__)

# MODO PYTHON

class ContaPython:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        ContaPython.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite  

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente: {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1  = ContaPython('Gervasio', 750, 2300)
conta2  = ContaPython('Cleitinho', 987, 15690)

print(conta1.extrato())
print(conta2.extrato())
  
soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é: {soma}')

print(conta1.__dict__)
conta1.limite = 666
print(conta1.__dict__)

print(conta1.valor_total)
