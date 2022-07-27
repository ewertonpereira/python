import time
from threading import Thread

contador = 50_000_000

def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(contador)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')
