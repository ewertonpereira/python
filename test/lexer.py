"""
TAREFA
Complementar o analisador para que reconheça:

Operadores Aritméticos: '+', '-', '*', '/', '^';
Comando de atribuição: '=';
Palavra reservada: 'if', 'while';
Delimitadores balanceados: '(', ')', '{', '}';
"""
import re

spec = [
    ('NUM', r'\d+(?:[\.,]\d+)?'),
    ('ID', r'[A-Za-z]+\d*'),
    ('ATRIB', r'[=]'),
    ('SKIP', r'[ \n\t]'),
    ('ADD', r'[+]'),
    ('SUB', r'[-]'),
    ('MUL', r'[*]'),
    ('DIV', r'[/]'),
    ('POW', r'[\^]'),
    ('LT', r'\<'),
    ('GT', r'\>'),
    ('LTE', r'\<='),
    ('GTE', r'\>='),
    ('EQ', r'=='),
    ('NEQ', r'<>'),
    ('IF', r'if'),
    ('VAR', r'var'),
    ('WHILE', r'while'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('COMMA', r','),
    ('SEMICOLON', r';'),
    ('ELSE', r'else'),
    ('INT', r'int'),
    ('REAL', r'real'),
]

tok = '|'.join('(?P<%s>%s)' % pair for pair in spec)
get_token = re.compile(tok).match


def lexico(codigo):
    val = get_token(codigo, 0)

    while val is not None:
        token = val.lastgroup
        lexema = val.group()
        if token != 'SKIP':
            if token == 'ID' and lexema.strip() in ['if', 'while', 'var', 'int', 'real']:
                token = lexema.strip().upper()
            elif token == 'ID':
                if re.match(r'^[A-Za-z]+$', lexema):
                    token = 'ID_VAR'
                else:
                    token = 'ID'
            yield ('TOKEN: %s\t VAL: %s' % (token, lexema))
        pos = val.end()
        val = get_token(codigo, pos)


# Código fornecido
def ler_codigo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        codigo = arquivo.read()
        
    return codigo


# Execute a análise léxica e sintática

codigo = ler_codigo('codigo.txt')


for token in lexico(codigo):
    print(token)
