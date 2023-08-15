"""
Desenvolver um aplicativo que converta de decimal para as bases hexadecial, octal e binária pelo método da subtração. O aplicativo deve demonstrar os cálculos passo a passo com o exemplo abaixo:

Subtração

1432052 = 1432052 - 1*16^5 = 383476

383476 = 383476 - 5*16^4 = 55796

55796 = 55796 - D*16^3 = 2548

2548 = 2548 - 9*16^2 = 244

244 = 244 - F*16^1 = 4

4 = 4 - 4*16^0 = 0

1432052 = 15D9F4

Decimal --> Hexadecimal
"""
from os import system


def clear(): 
    return system('cls')


def title() -> None:
    clear()
    width: int = 49
    print('=' * width)
    print(title := 'CONVERSOR'.center(width))
    print('=' * width)


def choose_base(choice: int) -> int:
    base: int = 0
    if choice == 1:
        base = 16
    elif choice == 2:
        base = 8
    elif choice == 3:
        base = 2
    return base


def menu_base() -> int:
    title()
    choice:int = 0
    print('\nEscolha o tipo de conversão que deseja fazer:')
    print('1 - Hexadecimal')
    print('2 - Octal')
    print('3 - Binária')
    try:
        choice: int = int(input('Digite a sua escolha: '))
    except:
            choice = menu_base()
    if choice not in [1, 2, 3]:
            choice = menu_base()
    return choice


def get_number_converter() -> int:
    title()
    number: int = 0
    try:
        number = int(input('\nAgora digite o número que deseja converter: '))
    except:
        number = get_number_converter()
    return number


def start() -> None:
    title()
    base: int = choose_base(menu_base())
    number:int = get_number_converter()
    title()
    print('\nO resultado é: '+''.join(custom_map((converter_division(converter(base, number))))))


def base_converter(base: int, power_meter: int) -> int:
    number: int= base ** power_meter
    return number


def converter(base: int, number_to_convert: int):
    power_meter: int = 0
    base_number: int = base_converter(base, power_meter)
   
    while base_number < number_to_convert:
        power_meter += 1
        converted_number = base_converter(base, power_meter)
        if converted_number > number_to_convert:
            power_meter -= 1
            data_list = [base, power_meter, number_to_convert, []]
            return data_list
        else:
            base_number: int = converted_number


def converter_division(list):
    counter: int = 1
    base_number: int = (counter * (list[0]**list[1]))
    number_to_convert: int = list[2]
    
    while base_number <= number_to_convert:
        counter += 1
        new_base_number = (counter * (list[0]**list[1]))
        
        if new_base_number > number_to_convert:
            list[3].append(counter-1)
            list[1] -= 1
            print(f'{list[2]}\t- {counter-1}x{list[0]}^{list[1]+1}\t= {(result := number_to_convert - base_number)}')
            list[2] = result
            # [base, power_meter, number_to_convert, [result]]
            list = [list[0], list[1], list[2], list[3]]
            converter_division(list)
            return list[3]
        else:
            base_number = new_base_number

    if base_number > number_to_convert:
        if list[1] >= 0:
            list[3].append(counter-1)
            list[1] -= 1
            print(f'{list[2]}\t- {counter-1}x{list[0]}^{list[1]+1}\t= {(result := list[2])}')
            list[2] = result
            list = [list[0], list[1], list[2], list[3]]
            converter_division(list)
            return list[3]
        

def custom_map(lst) -> list[str]:
    mapping: dict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    
    def apply_mapping(item) -> str:
        if item in mapping:
            return str(mapping[item])
        return str(item)
    
    mapped_list: list = list(map(apply_mapping, lst))
    return mapped_list
            

if __name__ == '__main__':  
    start()
    #5869572
    #1432052
