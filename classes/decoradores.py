"""
Decorators

O que são decorators?

- Decorators são funções;
- Decorators encolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos Higher Order Functions
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar)
"""
# Decorators como funções(Sintaxe não recomendada)

from pyclbr import Function


def seja_educado(function):
    def sendo():
        print('Foi um prazer conhecer você!')
        function()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo')


# Testando 1

teste = seja_educado(saudacao)
teste()

print(' ')

# Testando 2

def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)
raiva_educada()

print(' ')

# Decorators com Syntax Sugar

def seja_educado_mesmo(function):
    def sendo_mesmo():
        print('Foi um prazer conhecer você.')
        function()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentacao():
    print('Meu nome é Josemar')


# Testando 

apresentacao()

print(' ')

@seja_educado_mesmo
def dormir():
    print('Quero dormir.')


dormir()

print(' ')

# OBS: Não confunda decorator com decorator function