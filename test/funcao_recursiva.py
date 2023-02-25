from time import time

def factory_value(number: int):
    if number == 1:
        return 1
    else:
        return number * factory_value(number - 1)


print(result := factory_value(5))


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]

        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
        
        
print(quicksort([10, 5, 2, 3, 1, 65, 60, 0]))
