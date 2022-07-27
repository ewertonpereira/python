"""
Geradores

- Geradores (Generators) são iterators(Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
    - Generators podem ser criados com funções geradores;
    - Funções geradores utilizam a palavra reservada yield;
    - Generators podem ser criados com Expressões Geradoras;

Diferença entre Funções e Generator Functions

-------------------------------------------------------------------------------------
|Funções                                     |Generator Functions                   |
|Utilizam return                             |Utilizam yield                        |
|Retorna uma vez                             |Pode utilizar yield multiplas vezes   |
|Quando executada, retorna um valor          |Quando executada, retorna um generator|
-------------------------------------------------------------------------------------
"""
# Exemplo de Generation Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# OBS: Uma Generation Function não é um generator. Ela gera um Generator. ok!?

gen = conta_ate(5)

print(type(gen))
print(list(gen))

gen2 = conta_ate(10)

for number in gen2:
    print(number)

gen3 = list(conta_ate(10))

print(gen3)
