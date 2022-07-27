# math.prod - retorna o produto de um container numérico

import math, statistics
numbers_v1: int = [2, 3, 4, 6, 8]
numbers_v2: int = (2, 3, 4, 6, 8)
numbers_v3: int = {2, 3, 4, 6, 8}

print(numbers_v1 := math.prod([2, 3, 4, 6, 8])) # 2 * 3 * 4 * 6 * = 1152
print(math.prod(numbers_v2))
print(math.prod(numbers_v3))

# math.isqrt - Retorna a parte inteira da raiz quadrada de um número

print(raiz1 := math.isqrt(9))
print(raiz2 := math.sqrt(9))
print(raiz3 := math.isqrt(17))
print(raiz4 := math.sqrt(17))

# math.dist - retorna a distância euclidiana entre dois pontos, 3D ou 2D

# Pontos 3D

p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D

p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

# math.hypot - Retorna a hipotenusa, ou norma Euclidiana

print(math.hypot(*p3d1)) # * Descompacta 
print(math.hypot(*p2d1))

# Estatística

# statistics.fmean - Calcula a média de números reais

valores_reais: float = [1.45, 6.874, 2.6983]
valores_inteiros: int = [1, 6, 5, 89]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))

# statistics.geometric_mean - Calcula a média geométrica de números reais

print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))

# statistics.mulimode - Retorna o valor mais frequênte um uma sequência

seq1: str = 'Ewerton Pereira'
seq2: int = [1, 2, 2, 6, 5, 3, 5, 1 , 8, 8, 4]
seq3: int = [1, 2, 2, 6, 5, 3, 5, 1 , 8, 8, 4, 1]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
