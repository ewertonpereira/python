"""
Herança - Inheritance

A ideia de herança é a de reaproveitar código. Também extender nossa classes.

OBS: Com a herança, a partir de uma classe existente nós extendemos outra classe que passa a herdar 
atributos e métodos da classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula

Perguntar: Existe uma entidade genérica o suficiente para encapsular os atributos e métodos comuns a 
outras entidades?

OBS: Qunado uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:

    - Super Classe;
    - Classe Mãe:
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:

    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

# Sobrescrita de Métodos, ocorre quando reescrevemos/reimplementamos um método presente na super classe 
em classes filhas.


"""
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self,  nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        # Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa"""
    def __init__(self,  nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(f'CPF: {self._Pessoa__cpf}')
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'



cliente1 = Cliente('Ewerton', 'Pereira', '012345678910', 1702)
funcionario1 = Funcionario('Josebar', 'Fagundes', '012345678910', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

#print(cliente1.__dict__)
#print(funcionario1.__dict__)

# Sobrescrita de Métodos - Overriding

