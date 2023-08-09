number_to_convert: int = 1423

def base_converter(base: int, power_meter: int):
    number: int= base ** power_meter
    return number


def converter(base: int, number_to_convert: int):
    power_meter: int = 0
    counter: int = 1

    base_number = base_converter(base, power_meter)

    while base_number < number_to_convert:
        power_meter += 1
        new_number = base_converter(base, power_meter)
        if new_number > number_to_convert:
            power_meter -= 1
            break
        else:
            base_number = new_number

    new_m = (counter * (base_number))
    while base_number < number_to_convert:
        print(f'counter {counter}')
        counter += 1
        new_m2 = (counter * (base_number))
        if new_m2 > number_to_convert:
            power_meter -= 1
            break
        else:
            new_m = new_m2

    print(f'{base} {power_meter} ')
    
    print(new_m)

    return base_number



print(converter(16, number_to_convert))