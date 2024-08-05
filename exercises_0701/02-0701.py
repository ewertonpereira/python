"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre os valores lidos.
"""
'''
values = []
goal = 0

while goal < 6:
    number = int(input(f'Digite 6 números {goal+1}/6: '))
    values.append(number)
    goal +=1
    
print(values)'''

# update using claude as a pair programming

import os
from typing import List, NoReturn

def clear() -> int:
    # 'nt' stands for "New Technology", which is used for Windows systems
    # On Unix-based systems (like Linux or macOS), os.name is typically 'posix'
    return os.system('cls' if os.name == 'nt' else 'clear')

def get_integer_input(prompt: str, max_attempts: int = 3) -> NoReturn:
    for attempt in range(max_attempts):
        try:
            value: int = int(input(prompt))
            return value
        except ValueError:
            print(f"That's not a valid integer. Please try again. ({attempt + 1}/{max_attempts})")
    
    print("Maximum attempts reached. Exiting.")
    # Any non-zero exit status (like 1) typically indicates that some error or abnormal condition occurred.
    exit(1)

def main() -> None:
    clear()
    GOAL: int = 6

    print(f"Please enter {GOAL} integer values.")
    # while counter < goal:
    #     print(f'{counter + 1}/{goal}')
    #     vector.append(get_integer_input())
    #     counter += 1

    # List Comprehension -  Pythonic approach
    vector: List[int] = [get_integer_input(f"Enter integer {i+1}/{GOAL}: ") for i in range(GOAL)]

    print(f"\nThe entered values are: {vector}")

if __name__ == "__main__":
    main()
    