
from os import system


def clear() -> None: 
    return system('cls')


def title() -> None:
    clear()
    width: int = 49
    print('=' * width)
    print(title := 'CONVERSOR'.center(width))
    print('=' * width)


def cls_title() -> None:
    clear()
    title()


def choose_base() -> int:
    base: int = 0
    print('\nEscolha o tipo de conversão que deseja fazer:')
    print('1 - Hexadecimal')
    print('2 - Octal')
    print('3 - Binária')
    choice: int = int(input('Digite a sua escolha: '))
    if choice not in [1, 2, 3]:
        title()
        choice = choose_base()

    if choice == 1 or choice == 16:
        base = 16
    elif choice == 2 or choice == 8:
        base = 8
    elif choice == 3 or choice == 2:
        base = 2

    return base


def start ():
    cls_title()
    base: int =  choose_base()
    cls_title()
    number: int = int(input('\nAgora digite o número que deseja converter: '))
    cls_title()
    print(result := '\nO resultado é: '+''.join(custom_map((converter_division(converter(base, number))))))


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
