import random

name = input('Digite seu nome: ')
age = int(input('Digite sua idade: '))

while age < 0 or age > 100:
    age = int(input('Digite sua idade: '))
  
if age <= 15:
    print(f'\nDesculpe {name}, você é jovem demais para começar a investir.')
    if age == 15:
        print(f'\nMas te aguardo ano que vem {name}!!! \U0001F646')
elif age >= 16:
    print(f'{name}, você já pode fazer investimentos!!! \U0001F4B0')
    value = int(input('\nDigite o valor que dejesa investir: '))
    
    if value <= 0:
        print(f'\n{name} você é pobre \U0001F614')
    elif value <= 100:
        print(f'\n{value} é um ótimo para começar a investir! \U0001F60F')
    elif value <= 500:
        print(f'\nCom {value} você já esta bem encaminhado, continue fazendo seus investimentos. \U0001F61C')
    elif value >= 501:
        print(f'\n{name} você vai ser milionário em breve!!!')
        
    if value > 0:
        print(f'\nOnde deseja investir seu dinheiro {name}?')
        print("""
        1 - Poupança [investimentos nesta opção não possuem ricos, e taxa de valorizaçãO é de 0,5%% ao anoo] 
        2 - CDB [investimentos nesta opção não possuem riscos, e a taxa de valorização é de 1%% ao ano.]   
        3 - Ações [investimentos nesta opção tem riscos, e margem de lucro é variável.
        
        """)
            
        choice = float(input('Digite o numero da opção de sua preferência: '))
            
        pop = 0.05
        cdb = 0.1
        random.seed()
        acoes = random.randrange(1, 25) / 100
        #print(f'{acoes}')

        if choice == 1:
            value += (value * pop)
            print(f'{name}, o valor do seu dinheiro aplicado na poupança é R${value}')
        elif choice == 2:
            value += (value * cdb)
            print(f'{name}, o valor do seu dinheiro aplicado no CDB é R${value}')
        else:
            value += (value * acoes)
            print(f'\n{name}, o valor do seu dinheiro aplicado em ações é R${value}')
