"""
TAREFA
Complementar o analisador para que reconheça:

Operadores Aritméticos: '+', '-', '*', '/', '^';
Comando de atribuição: '=';
Palavra reservada: 'if', 'while';
Delimitadores balanceados: '(', ')', '{', '}';
"""
import re

spec = [    # Define as especificações da ER;
        ('NUM',  r'\d+(\.\d+)?'),
        ('ID',   r'[A-Za-z] +'),
        ('ATRIB',   r'[=]'),
        ('SKIP', r'[ \n\t]'),
        ('ADD', r'[+]'),
        ('MUL', r'[*]')
]

#  Concatenação das sequências de definões de <spec> em  um array e <compila> 
#  o padrão de expressão regular em um objeto expressão regular, que pode 
#  ser reutilizado várias vezes;
tok = '|'.join('(?P<%s>%s)' % pair for pair in spec)
get_token = re.compile(tok).match

def lexico(codigo):
  #  aplica o <match> do <get_token> para procurar um padrão 
  #  na string <codigo> a partir da posição 0;
  val=get_token(codigo,0)  

  while val is not None:
    token = val.lastgroup # token = último grupo encontrado no <match>
    lexema = val.group()  # lexema = grupo da correspondência
    if token != 'SKIP':   # Evita os símbolods indesejáveis
      yield('TOKEN: %s\t VAL: %s' %(token, lexema)) # retorna a estrutura
    pos = val.end()       # Reposiciona o próximo símbolo a ser testado
    val=get_token(codigo,pos) # Aplica o <match> para a sequencia


entrada = 'TOTAL = soma             while      45.0 + 56.34 * total/98'

for token in lexico(entrada):
    print(token)