"""
Módulo Collections - Deque

https://docs.python.org/3/library/collections.html#collections.deque

Podemos dizer que o Deque é uma lista de alta performance.


"""
from collections import deque

# Criando Deques

deq = deque('Ewerton')
print(deq)

# Adicionando elementos no deque

deq.append('z') # Adiciona no  final
print(deq)

deq.appendleft('k') # Adiciona no começo
print(deq)

# Remover elementos

print(deq.pop()) # Remove e retorna o último elemento
print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento
print(deq)
