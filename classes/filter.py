"""
Filter

filter() -> Serve para filtrar dados de uma certa coleção
"""
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, senso uma função e um iterável.

res = filter(lambda valor: valor > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória

paises = ['', 'Argentina', 'Brasil', '', 'Chile', 'Venezuela', '', '', 'Colombia']

res = filter(None, paises) # Better way - simple
print(list(res))

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

res = filter(lambda pais: pais != '', paises)
print(list(res))
"""
A diferença entre map() e filter() é:

map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento iterável.

filter() -> Recebe dois parâmetros, uma funçao e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função.

"""
# Exemplo mais complexo

user = [
    {'username':'ewerton', 'tweets':['Metal is the law', '#forabolsonaro']},
    {'username':'julia', 'tweets':['Me gusta marijuana', '#forabolsonaro']},
    {'username':'kerlen', 'tweets':['#forabolsonaro']},
    {'username':'paulinho', 'tweets':[]},
    {'username':'tonho', 'tweets':['#forabolsonarogenocida', '#forabolsonaro']},
]

# Filtrar os usuários que estão inativos no Twitter

# Forma 1

inativos = list(filter(lambda userx: len(userx['tweets']) == 0, user))
print(inativos)

# Forma 2

inativos = list(filter(lambda userx: not userx['tweets'], user))
print(inativos)

# Combinar filter() e map()

nomes = ['vanessa', 'anna', 'maria']

# Devemos criar uma lista contendo sua instrutora é' + o nome. Desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é: {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
