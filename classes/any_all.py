"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou se ainda se o iterável esta vázio.

"""
# Exemplo all()

print(all([0, 1, 2, 3, 4])) # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4])) # Todos os números são verdadeiros? True
print(all([])) # True

nomes = ['Ed', 'Ewerton', 'Eduarda']

print(all(nome[0] == 'E' for nome in nomes))
print(all([num for num in [4, 2, 10, 6, 8] if not num % 2]))
"""
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False  
"""
print(any([0, 1, 2, 3, 4])) # True
print(any([])) # False
