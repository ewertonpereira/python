"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy
data_final = dd/mm/yyyy

delta = data_final - data_inicial
"""
import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2023, 3, 3, 0)

# Calculando delta
tempo_para_evento = aniversario - data_hoje
print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento) # .days mostra apenas os dias
print('---------------')

data_compra = datetime.datetime.now()
print(data_compra)
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento_boleto = data_compra + regra_boleto
print(vencimento_boleto)
