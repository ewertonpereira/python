"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String para

Em Python, String é tudo que que estiver entre:
    - Aspas simples;
    - Aspas duplas;
    - Aspas triplas;
    
"""
#Entrada de dados
name = input('Qual seu nome?')

age = int(input('Qual sua idade?'))

#Saída de dados

#Exemplo de print antigo
print('Seja bem-vindo(a) %s, sua idade é %s anos' %(name, age))

#Exemplo de print novo
print('Seja bem-vindo(a) {0}, sua idade é {1} anos'.format(name, age))

#Exemplo de print atual
print(f'Seja bem-vindo(a) {name}, sua idade é {age} anos')

#Cast é a conversão de um tipo de dado para outro.

print(f'O {name} nasceu em {2021 - age}')
