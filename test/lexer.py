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
    ('ID', r'[A-Za-z]+'),
    ('ID_VAR', r'[A-Za-z]+'),
    ('ATRIB', r'[=]'),
    ('SKIP', r'[ \n\t]'),
    ('ADD', r'[+]'),
    ('SUB', r'[-]'),
    ('MUL', r'[*]'),
    ('DIV', r'[/]'),
    ('EXP', r'[\^]'),
    ('IF', r'if'),
    ('WHILE', r'while'),
    ('OPEN_PAREN', r'\('),
    ('CLOSE_PAREN', r'\)'),
    ('OPEN_BRACE', r'\{'),
    ('CLOSE_BRACE', r'\}'),
    ('COMMA', r','),
]

tok = '|'.join('(?P<%s>%s)' % pair for pair in spec)
get_token = re.compile(tok).match


def lexico(codigo):
    val = get_token(codigo, 0)

    while val is not None:
        token = val.lastgroup
        lexema = val.group()
        if token != 'SKIP':
            if token == 'ID' and lexema.strip() in ['if', 'while']:
                token = lexema.strip().upper()
            elif token == 'ID':
                token = 'ID_VAR'
            yield ('TOKEN: %s\t VAL: %s' % (token, lexema))
        pos = val.end()
        val = get_token(codigo, pos)


entrada = 'TOTAL = soma, while if  45.0 + 56,34 * = ^ total / 98'


for token in lexico(entrada):
    print(token)
