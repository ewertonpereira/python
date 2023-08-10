number_to_convert: int = 1432052
# 1423
# 1432052

def base_converter(base: int, power_meter: int):
    number: int= base ** power_meter
    return number


def converter(base: int, number_to_convert: int):
    power_meter: int = 0
    base_number = base_converter(base, power_meter)
   
    while base_number < number_to_convert:
        power_meter += 1
        new_number = base_converter(base, power_meter)
        if new_number > number_to_convert:
            power_meter -= 1
            list = [base, power_meter, number_to_convert]
            return list
        else:
            base_number = new_number


def basex(list):
    counter: int = 1
    base_number = (counter * (list[0]**list[1]))
    while base_number < number_to_convert:
        counter += 1
        print(o := (counter * (list[0]**list[1])))
        new_base_number = (counter * (list[0]**list[1]))
        if new_base_number > number_to_convert:
            list[1] -= 1
            print(f'{list[2]} - {counter-1}x{list[0]}^{list[1]+1} = {(result := number_to_convert - base_number)}')
            counter-=1
            list[2] = result
        else:
            base_number = new_base_number
            
    
basex(converter(16, number_to_convert))