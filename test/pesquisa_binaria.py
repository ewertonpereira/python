def create_number_list(number: int) -> list[int]:

    number_list: list[int] = []

    for i in range(0, number + 1):
        number_list.append(i)

    return number_list


number_list: list[int] = create_number_list(100)

def pesquisa_binaria(number_list: list[int]) -> str:
    min_number: int = number_list[0]+1
    max_number: int = number_list[len(number_list) - 1]
    goal: int = 0

    choice: int = int(input(f'Escolha um número entre {min_number} e {max_number}: '))

    adder : int = 0

    while goal != choice:

        goal: int = int((min_number + max_number) / 2)
        print(goal)

        if choice > goal:
            min_number = goal + 1
            adder += 1
        else:
            max_number = goal - 1
            adder += 1

    return f'O número escolhido foi: {goal}, e {adder} tentativas foram necessárias para descobrir o resultado.'


print(result := pesquisa_binaria(number_list))
