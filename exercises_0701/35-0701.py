"""
Faça um program que leia dois números, A e B(Positivos menores que 10000) e:

    - Crie um vetor onde cada posição é um algorismo do número. A primeira posição é o algoristimo menos significativo.

    - Crie um vetor que seja a soma de A e B, mas faça-o usando vetor construídos anteriormente.

Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia 10 do resultado e some 1 à proxima posição.
"""
min_size = 0
max_size = 1000
vector1 = []
vector2 = []

def tries():

    try:
        value = int(input('Digite um valor De 0 à 1000: '))

        if value <  min_size or value > max_size:
            value = tries()
        else:
            return value

    except ValueError as err:
        print('O valor de A deve ser um número inteiro!\n')
        value = tries()

    finally:
        return value 



a = tries()
b = tries()

#print(list(map(int, str(a))))
v1 = (list(map(int, str(a))))

#print(list(map(int, str(b))))
v2 = (list(map(int, str(b))))

for number in v1:
    vector1.append(number)


for number in v2:
    vector2.append(number)


print([number for number in vector1])
print([number for number in vector2])
