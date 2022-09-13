"""
2. Criptografia de mensagem. Essa cifra, consiste em girar as letras a partir de um seguinte número de posições. Sendo assim, a pessoa que recebe a mensagem, sabe quantas posições voltar, e portanto, terá a mensagem original. Sua tarefa é, dado um texto qualquer, realizar a rotação.

Obs: Não precisa considerar caracteres com acentos, como: á, à e etc…

Alfabeto: abcdefghijklmnopqrstuvwxyz

Exemplo:
texto = Ola, meu nome eh Carlos! e o Seu?
rotacoes = 7
resultado = Vsh, tlb uvtl lo Jhysvz! L v zlb?;

Sua implementação deve ter uma função que receba um número inteiro positivo(a rotação) e um texto,
e deve retornar o texto cifrado.

Exemplo:
std::string teste(int rotacoes, std::string texto) {
...
return
"""
from os import system


# clean terminal screen
def clear():
    return system('cls')


def rotation_number():
    try:
        rotation: int = int(input('Informe o número de rotações: '))
    except ValueError:
        clear()
        print('Digite apenas números inteiros')
        rotation: int = rotation_number()

    return rotation


rotation: int = rotation_number()
text: str = input('Digite seu texto: ')
print(text)

 
alphabet: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for letter in range(len(text)):
    for letter_ in range(len(alphabet)):
        if letter == letter_:
            text = text.replace(text[letter], alphabet[letter_ + rotation])
            


print(text)
