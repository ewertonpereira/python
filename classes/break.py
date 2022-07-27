"""
Saindo de loops com break

Funciona da m esma forma que nas linguagens C e Java.

Utilizamos o break para sair de loops de maneira projetada.


"""
# Exemplo 1

for num in range(1,11):
    if num == 6:
        break
    else:
        print(num)
print('Sai do loop')

# Exemplo 2

while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break
