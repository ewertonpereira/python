"""
Mapas -> Conhecidos em Python como dicionários

Dicionários em Python são representados por '{}'

#Interar sobre dicionários

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])
    
for chave in receita:
    print(f'{chave} : {receita[chave]}')
    
    #  Forma recomendável de mostrar as chaves em uso.
# Acessando as chaves 
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave = {chave} e valor = {valor}')



"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Soma*, valor máximo*, valor mínimo*, tamanho

print(sum(receita.values())) # Soma
print(max(receita.values())) # Valor máximo
print(min(receita.values())) # Valor mínimo
print(len(receita))        # Tamanho
