"""
Criando sua própria versão de loop
"""
def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Ewerton Pereira')

numbers = [1, 2, 3, 4, 5, 6]

meu_for(numbers)
