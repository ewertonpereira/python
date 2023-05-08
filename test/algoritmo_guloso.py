estados_abranger = set(['rs', 'sc', 'pr', 'sp', 'am', 'pi', 'rr', 'ro'])

estacoes = {}

estacoes['kum'] = set(['sp', 'am', 'pi'])
estacoes['kdois'] = set(['sp', 'rs', 'ro'])
estacoes['ktres'] = set(['sc', 'am', 'pr'])
estacoes['kquatro'] = set(['am', 'sc', 'rr'])
estacoes['kcinco'] = set(['pr', 'rr'])

estacoes_final = set()

while estados_abranger:

    melhor_estacao = None

    estados_cobertos = set()

    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger and estados_por_estacao

        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao

        estados_cobertos = cobertos
        estados_abranger -= estados_cobertos

        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao

        estacoes_final.add(melhor_estacao)

        
print(estacoes_final)