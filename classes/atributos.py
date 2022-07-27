"""
Atributos

Atributos -> Representam as características do objeto, ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

EMPython, dividimos os atributos em 3 grupo:

    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos.

# Atributo de instância: São atributos declarados dentro do método construtor.

OBS: Método construtor é um método especial utilizado para a construção do objeto.

# Em Java, uma classeLâmpada incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    privite int voltagem;
    private String cor;
    private Boolean ligada = false;

    public lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python, por conveção, ficou estabelicido que todo atributo de uma classe é público. Ouseja, pose
ser acessado em todo o projeto. Caso queiramos demonstrar que determinado a tributo deve ser tratado 
como privado, ou seja, que deve ser acessado/utilizado somente dentro da própria classe onde está 
declarado, utiliza-se __ duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling.


"""
# Classes com atributos de instância públicos

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

"""
    @property
    def voltagem(self):
        return self.__voltagem


    @property
    def cor(self):
        return self.__cor


    @property
    def ligada(self):
        return self.__ligada

"""
class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuaario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email - email
        self.senha = senha


# Classes com atributos de instância públicos e privados 

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# OBS: Lembre-se que isso é apenas uma conveção, ou seja, a linguagem Python não vai empedir que façamos 
# acessos os atributos sinalizados como privados fora da classe.

user = Acesso('user@bol.com', '1234')

print(user.email)
# print(user.__senha) # AttributeError

print(user._Acesso__senha) # Mostra a senha - Name Mangling

user.mostra_email()
user.mostra_senha()

# O que significa atributos de instância?

# Significa que ao criarmos instâncias de uma classe, todas as instâncias terão estes atributos

user1 = Acesso('user1@bol.com', '1234')
user2 = Acesso('user2@bol.com', '1234')

user1.mostra_email()
user2.mostra_email()

# Atributos de classe

p1 = Produto('Suco de caju', 'Suco', 5.99)
p2 = Produto('Cadeira Gamer', 'Cadeira', 1599.99)

"""
Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja, fora 
do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias
da classe. Ou seja, ao invéns de cada instância da classe ter seus príprios valores como é o caso dos
atributos da instância, com os atributos de classe todas as instâncias terão o mesmo valor para este atributo.
"""
# Refatorando a classe Produto

class ProdutoUpdate:

    #Atributo de classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = ProdutoUpdate.contador + 1 
        self.nome = nome
        self.descricao = descricao
        self.valor = round(valor * ProdutoUpdate.imposto, 2)
        ProdutoUpdate.contador = self.id


p3 = ProdutoUpdate('Heineken', 'Cerveja', 4.79)
p4 = ProdutoUpdate('New England', 'Cerveja', 13.90)

print(p3.valor) # Acesso possível, mas incorreto de um atributo de classe
print(p3.imposto)
print(p4.valor)
print(p4.imposto)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe.

print(ProdutoUpdate.imposto) # Acesso correto de um atributo de classe
print(p3.id)
print(p4.id)

# OBS: Em linguagens como o JAva, os atributos conhecidos como atributos de classe aqui em Python são chamados atributos estáticos.

# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução

# OBS: O atributo dinâmico será exclusivo da instância que a criou.

# Criando um atributo dinâmico em tempo de execução

p3.peso = '0.05kg' # Note que na classe ProdutoUpdate não existe peso

print(f'Produto {p3.nome}, Descrição: {p2.descricao}, Valor: {p3.valor}, Peso: {p3.peso}')

# Deletando atributos

print(p3.__dict__)
print(p4.__dict__)

del p3.peso

print(p3.__dict__)
print(p4.__dict__)
