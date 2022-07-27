"""
Definindo Funções

Funções são pequenas partes de código que realizam tarefas específicas. Pode ou não receber entradas 
de dados e retornar uma saída de dados. Elas são muito úteis par aexecutar procedimentos similares por repetidas vezes.

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação 
para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos este curso:
    - print();
    - len();
    - max();
    - min();
    - etc.

Em Python a forma geral de definir uma função é:

def nome_funcao(parametro_entrada):
    bloco_funcao
    
Nome da função sempre com letras minúsculas, se for um nome composto, palavra separada por underline(Snake Case)

Parâmetros de entrada são opcionais, onde tendo mais de um, devem ser separados por vírgula

Bloco da função,  é onde o processamento da função acontece. pode terou não retorno da função.

OBS: Veja quepara definir uma função utilizamos a palavra reservada 'def', informando ao Python que estamos definindo
uma função, também abrimos o bloco de código com o já conhecido dois pontos':', que é utilizado em Python 
para definir blocos.

"""
# Definindo a primeira função

def diz_oi():
    print('Oi')
    
# Veja que dentro das nossas funções podemos utilizar outras funções.
# Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer 'oi'.
# Veja que esta função não recebe nenhum parâmetro de entrada.
# Veja que esta função não retorna nada.

# Utilizando funções

def parabens():
    print('Parabéns pra você!')
    
for n in range(4):
    parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável.

diga = parabens

diga()
