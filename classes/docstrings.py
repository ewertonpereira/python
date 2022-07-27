"""
Documentando funções com Docstring

OBS: podemos ter acesso a documentação de uma função em Python utulizando a propriedade especial __doc__

Podemos ainda fazer acesso à documentação com a função help()
"""

# Exemplos

def diz_oi():
    """Uma função simples que retorna a string oi"""
    return 'Oi'


print(diz_oi())

def exponencial(num, potencia=2):
    """[Função que retorna por padrão o quadrado de 'num']

    Args:
        num ([type]): [número que queremos gerar o exponecial]
        potencia (int, optional): [Potência que queremos gerear o exponencial]. Defaults to 2.

    Returns:
        [type]: [Retorna o exponencial de 'num' por 'potencia']
    """
    return num**potencia

print(help(exponencial))
