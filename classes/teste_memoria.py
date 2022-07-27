"""
Teste de memória com Genetators

Sequência de Fibonacci:
1, 1, 2, 3, 5, 8, 13... n
"""

# Função usando listas - 449MB

def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

print([num for num in fib_list(10)])

# Função usando geradores - 3MB
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b =  b, a + b
        yield a
        contador += 1


print([num for num in fib_gen(10)])
