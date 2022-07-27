"""
Len, Abs, Sum ,Roud

# Len

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

Por debaixo dos panos , quando utilizamos a função len(), o Python faz o segunte:
"""
print('Ewerton Pereira'.__len__()) # Dunder len

"""
# Abs

abs() -> Retorna o valor absuloto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.
"""
print(abs(-5))
print(abs(5))
print(abs(-3.14))
print(abs(3.14))
"""
# Sum

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total
dos elementos, incluindo o valor inicial.

# OBS: O valor inicial default = 0
"""
# Exemplos

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5)) # Com valor inicial

print(sum([3.145, 5.678]))

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))
"""
# Round

round() -> Retorna um número um número arrredondado para n digito de precisão após a casa decimal. Se 
a precisão não for informada retorna o inteiro mais próximo da entrada.
"""
# Exemplos

print(round(10.2))

print(round(10.5)) # 0,5 arredonda para baixo

print(round(10.6)) # 0,6 arredonda para cima

print(round(10.2121212121, 2))

print(round(10.21999999, 2))
