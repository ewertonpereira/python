"""
Faça um programa para ler 10 números Diferentes a serem armazenados em um vetor. Os números deverão ser amazenados no vetor na ordem que forem lidos, sendo que caso que o usuário digite um 
número que ja foi digitado abteriormente, o programa deverá pedir para que ele digite outro número. Note que cada valor digitado pelo usúario deve ser pesquisado no vetor, verifique se ele existe entre os números que
já foram fornecidps. Exibir na tela o valor final que foi digitado.
"""
size = 10
vector = []

def verify(number, vector):

    if number in vector:
            num = int(input(f'Digite outro número, este já existe {len(vector) + 1}/{size}: '))
            verify(num, vector)
    else:
        vector.append(number)

while len(vector) < size:

    number = int(input(f'Digite um número para o vetor {len(vector) + 1}/{size}: '))

    verify(number, vector)
            

print([number for number in vector])
