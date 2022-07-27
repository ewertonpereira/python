from concurrent.futures import process
from multiprocessing import Pool
import time

contador = 50_000_000

def contagem_regressiva(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [contador//2])
    r2 = pool.apply_async(contagem_regressiva, [contador//2])
    pool.close()
    pool.join()
    fim = time.time()
    print(f'Tempo em segundos {fim - inicio}')
