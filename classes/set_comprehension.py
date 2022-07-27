"""
Set Comprehension

"""
# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplos

numeros = {x ** 2 for x in range(10)}
print(numeros)


# DESAFIO: Faça uma alteração na estrutura acima para gerar um dicionário ao invéz de set

print({x: x ** 2 for x in range(10)})

# String

letras = {letra for letra in 'Ewerton Pereira'}
print(letras)
