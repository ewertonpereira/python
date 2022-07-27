"""
Por que testar nosso código?

    - Reduzir bugs no código existente;
    - Garantem que novos recursos da sua aplicaão não quebrem recursos antigos;
    - Garantem  que bugs que foram corrigidos anteriormente continuem corrigidos;
    - Garantetm que a refatoração que costumamos fazer não tragam novos bugs;

TDD - Test Driven Development - Desenvolvimento Guiado por Testes

COM TDD  é utilizado estágios de desenvolvimento:

    - Você escreve seu teste primeiro;
    - Então você escreve o código mínimo suficiente para fazer o teste passar/executar;
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Esses estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:

    - Red;
    - Green;
    - Refactor;


Testes automatizados! 
"""
class Gato:

    def __init__(self, nome):
        self.__nome = nome 

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')


jarbas = Gato('Jarbas')
jarbas.miar()
print(jarbas.nome)
