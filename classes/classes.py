"""
Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagne que você queira fazer um sistema para automatizar o controle das lampadas da sua casa.

Classes podem conter:

    - Atributos -> Representam as características do objeto, ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmenteiríamos querer
    saber se a lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual a 
    liminosidade dela e etc.

    - Métodos -> Representão os comportamentos do objeto, ou seja, as ações que esse oobjeto pode realizar
    no se sistema. No caso da lâmpada, por exemplo, um comportamento mito comum que muito provavelmente
    iríamos querer representar no nosso  sistema é o ligar e desligar.

Em Python para definir uma classe utilizamos a palavra reserva class.

OBS: Utilizamos a palavra pass em Python quando temos um bloco de código que ainda não esta implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial maiúsculo. 
se o nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo, todas juntas.

Dica Geek: Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares para
nomes de classe, atributos, métodos, arquivos, diretórios e etc.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos
esses objetos que serão mapeados para classes de entidade.
"""
class Lampada:
    pass


lamp = Lampada()
print(type(lamp))
