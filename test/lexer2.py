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
    pos = 0
    val = get_token(codigo, pos)

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
            yield (token, lexema)
        pos = val.end()
        val = get_token(codigo, pos)
    
    # Remover espaços em branco
    codigo = codigo.replace(' ', '')






def ler_codigo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        codigo = arquivo.read()
        
    return codigo


def termo(tokens):
    if tokens[0][0] == 'ID' or tokens[0][0] == 'NUM':
        termo = tokens[0]
        return termo
    else:
        raise SyntaxError('Termo inválido. Identificador ou número esperado.')


def expressao_aritmetica(tokens):
    termo_esquerda = termo(tokens)
    while len(tokens) > 1 and tokens[1][0] in ['ADD', 'SUB', 'MUL', 'DIV', 'POW']:
        operador = tokens[1][0]
        tokens = tokens[2:]
        termo_direita = termo(tokens)
        termo_esquerda = ('expressao_aritmetica', termo_esquerda, operador, termo_direita)
    return termo_esquerda



def comando(tokens):
    if tokens[0][0] == 'ID':
        identificador = tokens[0][1]
        tokens = tokens[1:]

        if tokens[0][0] != 'ATRIB':
            raise SyntaxError('Operador de atribuição esperado.')

        tokens = tokens[1:]

        expressao = expressao_aritmetica(tokens)
        if expressao is None:
            raise SyntaxError('Expressão aritmética inválida.')

        if tokens[0][0] != 'SEMICOLON':
            raise SyntaxError('Ponto e vírgula esperado no fim da atribuição.')

        tokens = tokens[1:]

        return ('atribuicao', identificador, expressao)
    
    elif tokens[0][0] == 'IF':
        # Reconhecer comando if
        tokens = tokens[1:]  # Consumir o token 'if'

        # Verificar a condição do if
        if tokens[0][0] != 'LPAREN':
            raise SyntaxError('Falta abrir parênteses na condição do if.')
        tokens = tokens[1:]

        condicao = expressao_aritmetica(tokens)
        if condicao is None:
            raise SyntaxError('Condição do if inválida.')

        if tokens[0][0] != 'RPAREN':
            raise SyntaxError('Falta fechar parênteses na condição do if.')
        tokens = tokens[1:]

        # Verificar o corpo do if
        if tokens[0][0] != 'LBRACE':
            raise SyntaxError('Falta abrir chave no corpo do if.')
        tokens = tokens[1:]

        corpo_if = []

        while tokens[0][0] != 'RBRACE':
            comando_if = comando(tokens)
            corpo_if.append(comando_if)

        tokens = tokens[1:]  # Consumir o token '}' após o fim do corpo do if

        # Verificar o else, caso exista
        if tokens[0][0] == 'ELSE':
            tokens = tokens[1:]  # Consumir o token 'else'

            # Verificar o corpo do else
            if tokens[0][0] != 'LBRACE':
                raise SyntaxError('Falta abrir chave no corpo do else.')
            tokens = tokens[1:]

            corpo_else = []

            while tokens[0][0] != 'RBRACE':
                comando_else = comando(tokens)
                corpo_else.append(comando_else)

            tokens = tokens[1:]  # Consumir o token '}' após o fim do corpo do else

            return ('if_else', condicao, corpo_if, corpo_else)
        else:
            return ('if', condicao, corpo_if)

    elif tokens[0][0] == 'WHILE':
        # Reconhecer comando while
        tokens = tokens[1:]  # Consumir o token 'while'

        # Verificar a condição do while
                # Verificar a condição do while
        if tokens[0][0] != 'LPAREN':
            raise SyntaxError('Falta abrir parênteses na condição do while.')
        tokens = tokens[1:]

        condicao = expressao_aritmetica(tokens)
        if condicao is None:
            raise SyntaxError('Condição do while inválida.')

        if tokens[0][0] != 'RPAREN':
            raise SyntaxError('Falta fechar parênteses na condição do while.')
        tokens = tokens[1:]

        # Verificar o corpo do while
        if tokens[0][0] != 'LBRACE':
            raise SyntaxError('Falta abrir chave no corpo do while.')
        tokens = tokens[1:]

        corpo_while = []

        while tokens[0][0] != 'RBRACE':
            comando_while = comando(tokens)
            corpo_while.append(comando_while)

        tokens = tokens[1:]  # Consumir o token '}' após o fim do corpo do while

        return ('while', condicao, corpo_while)

    elif tokens[0][0] == 'LPAREN':
        # Reconhecer expressão aritmética
        expressao = expressao_aritmetica(tokens)
        if tokens[0][0] != 'RPAREN':
            raise SyntaxError('Falta fechar parênteses na expressão aritmética.')
        tokens = tokens[1:]
        return expressao

    else:
        raise SyntaxError(f'Comando inválido: {tokens[0][1]}')


# Lendo o código do arquivo
codigo = ler_codigo('codigo.txt')

# Realizando a análise léxica
tokens = list(lexico(codigo))

# Realizando a análise sintática
comando_result = comando(tokens)
print(comando_result)
