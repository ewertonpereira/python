# import re

# # Defina as especificações dos tokens e as funções auxiliares (match e lexico) conforme o código fornecido

# spec = [
#     ('NUM', r'\d+(\.\d+)?'),
#     ('ID', r'[A-Za-z]+'),
#     ('ATRIB', r'='),
#     ('SKIP', r'[ \n\t]'),
#     ('ADD', r'\+'),
#     ('SUB', r'-'),
#     ('MUL', r'\*'),
#     ('DIV', r'/'),
#     ('POW', r'\^'),
#     ('LT', r'\<'),
#     ('GT', r'\>'),
#     ('LTE', r'\<='),
#     ('GTE', r'\>='),
#     ('EQ', r'=='),
#     ('NEQ', r'<>'),
#     ('LPAREN', r'\('),
#     ('RPAREN', r'\)'),
#     ('LBRACE', r'\{'),
#     ('RBRACE', r'\}'),
#     ('COMMA', r','),
#     ('SEMICOLON', r';'),
#     ('IF', r'if'),
#     ('ELSE', r'else'),
#     ('WHILE', r'while'),
#     ('INT', r'int\b'),
#     ('REAL', r'real')
# ]

# tok = '|'.join('(?P<%s>%s)' % pair for pair in spec)
# get_token = re.compile(tok).match


# def match(tokens, expected_token):
#     if tokens and tokens[0][0] == expected_token:
#         tokens.pop(0)
#     else:
#         raise SyntaxError(f"Expected token {expected_token}, but found {tokens[0][0]}")


# def lexico(codigo):
#     pos = 0  # Adicione essa linha
#     val = get_token(codigo, pos)
#     while val is not None:
#         token = val.lastgroup
#         lexema = val.group()
#         if token != 'SKIP':
#             print('TOKEN: %s\t VAL: %s' % (token, lexema))  # Comando de impressão adicionado
#             yield ('TOKEN: %s\t VAL: %s' % (token, lexema))
#         pos = val.end()  # Atualize a posição
#         val = get_token(codigo, pos)  # Use a posição atualizada




# # Execute a análise léxica e sintática

# def programa(tokens):
#     declaracoes(tokens)
#     comandos(tokens)


# def declaracoes(tokens):
#     if tokens and tokens[0][0] in ['INT', 'REAL']:
#         tipo(tokens)
#         lista_variaveis(tokens)
#         match(tokens, 'SEMICOLON')
#         declaracoes(tokens)


# def tipo(tokens):
#     if tokens[0][0] == 'INT':
#         match(tokens, 'INT')
#     elif tokens[0][0] == 'REAL':
#         match(tokens, 'REAL')


# def lista_variaveis(tokens):
#     variavel(tokens)
#     if tokens[0][0] == 'COMMA':
#         match(tokens, 'COMMA')
#         lista_variaveis(tokens)


# def variavel(tokens):
#     match(tokens, 'ID')


# def comandos(tokens):
#     if tokens:
#         comando(tokens)
#         comandos(tokens[1:])  # Chamada recursiva com a lista de tokens restante


# def comando(tokens):
#     if tokens[0][0] == 'ID':
#         atribuicao(tokens)
#     elif tokens[0][0] == 'WHILE':
#         repeticao(tokens)
#     elif tokens[0][0] == 'IF':
#         fluxo_controle(tokens)


# def fator(tokens):
#     if tokens[0][0] == 'NUM':
#         match(tokens, 'NUM')
#     elif tokens[0][0] == 'ID':
#         match(tokens, 'ID')
#     elif tokens[0][0] == 'LPAREN':
#         match(tokens, 'LPAREN')
#         expressao(tokens)
#         match(tokens, 'RPAREN')
#     else:
#         raise SyntaxError(f"Invalid fator: {tokens[0][0]}")


# def termo(tokens):
#     fator(tokens)
#     while tokens and tokens[0][0] in ['MUL', 'DIV']:
#         match(tokens, tokens[0][0])
#         fator(tokens)


# def expressao(tokens):
#     termo(tokens)
#     while tokens and tokens[0][0] in ['ADD', 'SUB']:
#         match(tokens, tokens[0][0])
#         termo(tokens)


# def expressao_relacional(tokens):
#     expressao(tokens)
#     if tokens and tokens[0][0] in ['LT', 'GT', 'LTE', 'GTE', 'EQ', 'NEQ']:
#         match(tokens, tokens[0][0])
#         expressao(tokens)


# def atribuicao(tokens):
#     match(tokens, 'ID')
#     match(tokens, 'ATRIB')
#     expressao_relacional(tokens)
#     match(tokens, 'SEMICOLON')


# def repeticao(tokens):
#     match(tokens, 'WHILE')
#     match(tokens, 'LPAREN')
#     expressao_relacional(tokens)
#     match(tokens, 'RPAREN')
#     match(tokens, 'LBRACE')
#     comandos(tokens)
#     match(tokens, 'RBRACE')


# def fluxo_controle(tokens):
#     match(tokens, 'IF')
#     match(tokens, 'LPAREN')
#     expressao_relacional(tokens)
#     match(tokens, 'RPAREN')
#     match(tokens, 'LBRACE')
#     comandos(tokens)
#     match(tokens, 'RBRACE')


# # Crie uma função para ler o conteúdo do arquivo de código-fonte

# def ler_codigo(nome_arquivo):
#     with open(nome_arquivo, 'r') as arquivo:
#         codigo = arquivo.read()
        
#     return codigo


# # Execute a análise léxica e sintática

# codigo = ler_codigo('codigo.txt')
# tokens = list(lexico(codigo))
# programa(tokens)

# def analisador_lexico(codigo):
#     tokens = list(lexico(codigo))
#     caracteres_reconhecidos = ' '.join(token[1].strip() for token in tokens if token[0] != 'SKIP')
#     print(caracteres_reconhecidos)

#     # Verificar caracteres não reconhecidos
#     codigo_limpado = re.sub(r'\s', '', codigo)  # Remove espaços em branco
#     caracteres_nao_reconhecidos = re.findall(r'[^ \n\t]', codigo_limpado)
#     if caracteres_nao_reconhecidos:
#         print('Caracteres não reconhecidos: %s' % ' '.join(caracteres_nao_reconhecidos))
#     else:
#         print('Todos os caracteres foram reconhecidos.')


# analisador_lexico(codigo)

import re

def analisador_lexico(codigo):
    spec = [
        ('NUM', r'\d+(\.\d+)?'),
        ('ID', r'[A-Za-z]+'),
        ('ATRIB', r'='),
        ('SKIP', r'[ \n\t]'),
        ('ADD', r'\+'),
        ('SUB', r'-'),
        ('MUL', r'\*'),
        ('DIV', r'/'),
        ('POW', r'\^'),
        ('LT', r'\<'),
        ('GT', r'\>'),
        ('LTE', r'\<='),
        ('GTE', r'\>='),
        ('EQ', r'=='),
        ('NEQ', r'<>'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
        ('COMMA', r','),
        ('SEMICOLON', r';'),
        ('IF', r'if'),
        ('ELSE', r'else'),
        ('WHILE', r'while'),
        ('INT', r'int\b'),
        ('REAL', r'real')
    ]

    def lexico(codigo):
        pos = 0
        val = get_token(codigo, pos)
        tokens = []
        while val is not None:
            token = val.lastgroup
            lexema = val.group()
            if token != 'SKIP':
                print('TOKEN: %s\t VAL: %s' % (token, lexema))
                tokens.append((token, lexema))
            pos = val.end()
            val = get_token(codigo, pos)
        return tokens

    

    tok = '|'.join('(?P<%s>%s)' % pair for pair in spec)
    get_token = re.compile(tok).match

    tokens = lexico(codigo)
    caracteres_reconhecidos = ' '.join(token[1] for token in tokens if token[0] != 'SKIP')
    print('Caracteres reconhecidos: %s' % caracteres_reconhecidos)

    codigo_limpado = re.sub(r'\s', '', codigo)
    caracteres_nao_reconhecidos = re.findall(r'[^ \n\t]', codigo_limpado)

    if caracteres_nao_reconhecidos:
        print('Caracteres não reconhecidos: %s' % ' '.join(caracteres_nao_reconhecidos))
    else:
        print('Todos os caracteres foram reconhecidos.')


# Código fornecido
def ler_codigo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        codigo = arquivo.read()
        
    return codigo


# Execute a análise léxica e sintática

codigo = ler_codigo('codigo.txt')

# Chamada para realizar a análise léxica
analisador_lexico(codigo)


