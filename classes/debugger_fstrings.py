from audioop import mul
from unittest import result


def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2

resultado: float = multiplicar(4.66644, 6.4845)

print(f'O resultado é {resultado:.2f}')
print(f'O resultado é {(resultado := multiplicar(4.66644, 6.4845)):.2f}')

# Forma de mostrar variável e seu valor
name: str = 'Ewerton'

print(f'{name=}')
print(f'{name.upper()[::-1]=}')
