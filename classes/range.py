"""
Ranges

    - Precisamos saber o loop for para usar os ranges
    - Precisamos conhecer o range para trabalhar melhor com os loops for.

Ranges são utilizados para gerar sequência numéricas, não de forma aleatória, mas sim de forma especificada.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não incluso (início padrão 0, e passo de 1 em 1).

# Forma 1

for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

for num in range(1, 11):
    print(num)
    
# Fomar 3

range(valor_de_inicio, valor_de_parada, passo)

for num in range(5, 55, 5):
    print(num)
    
# Forma 4 (inversa)

range(valor_de_inicio, valor_de_parada, passo)

for num in range(10, 0, -1):
    print(num)
    

"""

