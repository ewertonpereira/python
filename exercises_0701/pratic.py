"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes desse vetor, armazenando o resultado em outro vetor.
Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
"""
from typing import Union, List
import math
import os
import numpy as np


def clear() -> int:
    return os.system('cls' if os.name == 'nt' else 'clear')


def get_number_input(prompt: str, max_attempts: int = 3) -> Union[int, float]:
    for attempt in range(max_attempts):
        try:
            value: Union[int, float] = float(input(prompt))
            if value.is_integer(): # Check if the float value is actually an integer
                return int(value)
            return value
        except ValueError:
            print(f"That's not a valid number. Please try again. ({attempt + 1}/{max_attempts})")
    
    print("Maximum attempts reached. Exiting.")
    exit(1)


def array_union(array_1:List[Union[int, float]], 
                array_2:List[Union[int, float]]) -> None:

    if len(array_1) != len(array_2):
        raise ValueError("Both arrays must have the same length")
        
    # Convert the lists to numpy arrays
    arr1 = np.array(array_1)
    arr2 = np.array(array_2)

    # Combine the arrays side by side
    combined = np.column_stack((arr1, arr2))
    
    [print(number) for number in combined]


def main() -> None:
    clear()
    GOAL: int = 10

    print(f"Please enter {GOAL} integer values.")
    vector_1: List[int] = [get_number_input(f'Enter integer {i+1}/{GOAL}: ') for i in range(GOAL)]
    vector_2: List[Union[int, float]] = [math.pow(number, 2) for number in vector_1]

    # diferent ways to show the result

    #print(*vector_1, sep='\n')
    #[print(num) for num in vector_2]
    #list(map(print, vector_1))
    array_union(vector_1, vector_2)


if __name__ == '__main__':
    main()
