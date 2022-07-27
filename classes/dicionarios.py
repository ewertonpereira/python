"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves '{}'

OBS: Sobre dicionários
    - Chave/valor são separados por 'chave: valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado ;
    - Podemos misturar tipos de dados;
"""
# Criação de dicionários

# Forma 1 - Mais comum

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)

# Forma 2 - Menos comum

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)

# Acessando elementos

# Forma 1 - Acesssando via chave, da mesma forma que lista/tupla

print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentamos fazer um acesso com uma chave que não existe, teremos um erro KeyError.

# Forma 2 - Acessando via get - RECOMENDADO

print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('ru')

# Caso o get não encontre o objeto com a chave informada, será retornada o valor NOne e não será gerado KeyError

if pais:
    print(f'encontrei o país {pais}')
else:
    print('Não encontrei o país')
    
    
pais = paises.get('py', 'Não encontrado') # SEGUNDO PARÂMETREO DEFINE UMA RESPOSTA CASO NÃO ENCONTRE A CHAVE
print(f'Encontrei o país {pais}')

# OBS: Podemos definir um valor padrão, para caso não encontremos o objeto com a cha informada.

# Podemos verificar se determinada chave se encontra em um dicionário.

print('br' in paises)     # True
print('ru' in paises)     # False
print('Brasil' in paises) # False

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean, list, tuple, dict) como chaves de dicionários.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas são imutáveis.localidades
localidades = {
    (35.6865, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova Iorque',
    (37.6885, 23.2536): 'Escritório em São Paulo',
}

print(localidades)

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300} 
print(receita)

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# Forma 2

novo = {'mai': 500}

receita.update(novo) # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550
print(receita)

receita.update({'mai': 600})
print(receita)

# Conclusão 1: a forma de adicinar novos elementos ou atualizar dados em dicionários é a mesma.
# Conclusão 2: Em dicionários, não podemos ter chaves repetidas.

# Remover dados de um dicionário

# Forma 1 - Mais comum

receita.pop('mar')
print(receita)

# OBS: aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é encontrado.

# Forma 2

del receita['fev']
print(receita)

# Se a chave não existir será gerado um KeyError.
# Neste caso o valor removido não é retonado.

# Imagine que você tem um comércio eletrôico, onde temos um carrinho de compras onde adicionamos produtos.

"""
Carrinho de compras:
    Produto1:
        - Nome;
        - Quantidade;
        - Preço.
    Produto 2:
        - Nome;
        - Quantidade;
        - Preço.
"""    

# Poderíamos utilizar uma lista para isso? sim.

carrinho = []
produto1 = ['Playstation 4', 1, 5030.00] 
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Teríamo que saber qual é o índice de cada impormação do produto.

# Poderíamos utilizar uma tupla para isso? Sim

produto1 = ('Playstation 4', 1, 5300.00)
produto2 = ('God of War', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

# Poderíamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'Nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 5030.00}
produto2 = {'Nome': 'God of War 4', 'Quantidade': 1, 'Preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Desta forma,  facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza sobre cada informação .

# Imagine que você tem um comércio eletrôico, onde temos um carrinho de compras onde adicionamos produtos.

"""
Carrinho de compras:
    Produto1:
        - Nome;
        - Quantidade;
        - Preço.
    Produto 2:
        - Nome;
        - Quantidade;
        - Preço.
"""       
# Poderíamos utilizar uma lista para isso? sim.

carrinho = []
produto1 = ['Playstation 4', 1, 5030.00] 
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Teríamos que saber qual é o índice de cada impormação do produto.

# Poderíamos utilizar uma tupla para isso? Sim

produto1 = ('Playstation 4', 1, 5300.00)
produto2 = ('God of War', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

# Poderíamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'Nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 5030.00}
produto2 = {'Nome': 'God of War 4', 'Quantidade': 1, 'Preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Desta forma,  facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza sobre cada informação .

# Métodos de dicionários

d = dict(a=1, b=2, c=3)
print(d)

# Limpar o dicionário(Zerar dados)

d.clear()
print(d)

# Copiando um dicionário para outro

# Forma 1 - Deep Copy
novo = d.copy() 
print(novo)

novo['d'] = 4
print(novo)

# Forma 2 - Shallow Copy

novo = d
print(novo)

novo['d'] = 5
print(d)
print(novo)


# Forma não usual de crição de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

# OBS: o método fromkeys recebe dos parâmetros: um iterável e uma valor.
# Ele vai gerar para cada valor do iterável e irá atribuir a essa chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja) # Não imprime o (TE) pois não existe repetição de chave em dicionários.

veja = {}.fromkeys(range(1,11), 'novo')
print(veja)
