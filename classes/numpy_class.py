import numpy as np


""" 
tipos de arrays: ndarrays -> significam arrays com N dimenções

1-D array -> Possui apenas uma dimensão. Será comumente chamado de vetor ou vector
2-D array -> Possui duas dimensões. Será comumente chamado de matriz ou matrix
3-D array -> Possui três ou mais  dimensões. Será comumente chamado de tensor

"""
# criando um array -> numpy.array()
print(a := np.array([1, 2, 3, 4, 5]))
print(f'{type(a)}\n') # class 'numpy.ndarray'
print(b := np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]), '\n')

# 3 = ndarray quantidade, 5 = quantidade de linhas, 6 = quantidade de colunas
print(result := np.zeros(shape=(3, 5, 6)),'\n')

# cria matrix
print(result := np.ones((2,3)),'\n')

# cria matrix vazia
print(result := np.empty((2,2)),'\n')

# cria linha popolada -> start - stop - step - type
print(result := np.arange(start=10, stop=55, step=5, dtype=int),'\n')

# divisão linear
print(result := np.linspace(start=0, stop=100, num=40, endpoint=False), '\n')

# descobrir informações
print(result := np.zeros(shape=(3, 5, 6)),'\n')
print('shape:\n', result.shape) # shape
print('size:\n', result.size) # quantidade de elementos
print('ndim:\n', result.ndim, '\n---------------------') # número de dimensões

print( result1 := np.array([1, 2, 3]), '\n---------------------')
# cria uma nova dimensão
print('matrix:\n',result := result1[np.newaxis, :])
print('shape:\n', result.shape)
print('ndim:\n', result.ndim, '\n---------------------')

# inverte 
print('matrix:\n', result := result1[:, np.newaxis])
print('shape:\n', result.shape)
print('ndim:\n', result.ndim)

# consultando itens de um array
print(result[1][0], '\n---------------------')

# concatenado arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(result := np.concatenate((a, b)))
print(result := np.concatenate((b, a)), '\n---------------------')

# consultando itens de um array com regra
print(result := np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), '\n')

print(maior_8 := result[result > 8], '\n---------------------') # result[result > 8] -> importante

print(result := a.sum())
print(result := a.max())
print(result := a.min())
print(result := a.mean(), '\n---------------------')

# gereando amostras aleatórias
from numpy.random import default_rng


rng = default_rng()
print(random := rng.integers(50, size=(2, 4)), '\n---------------------')

# diferença entre arrays e listas

# array -> sempre o mesmo tipo de dados

# lista -> podem ser dados variaddos

# comparando processamento

from time import process_time
# t1 = process_time()
lista1 = list(rng.integers(10, 100, 10000000))
# print((t2 := process_time()) - t1)
lista2 = list(rng.integers(10, 100, 10000000))
c = []

t1 = process_time()
for i in range(len(lista1)):
    c.append(lista1[i] * lista2[i])
print('list: ', (t2 := process_time()) - t1)


# t1 = process_time()
arraya = rng.integers(10, 100, 10000000)
# print((t2 := process_time()) - t1)
arrayb = rng.integers(10, 100, 10000000)

t1 = process_time()
c = a * b
print('array: ',(t2 := process_time()) - t1)

# import matplotlib.pyplot as plt

# dados_x = rng.integers(20, size=30)
# dados_y = rng.integers(12, size=30)

# plt.scatter(x=dados_x, y=dados_y)
# plt.show()
