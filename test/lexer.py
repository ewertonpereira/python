import re
from typing import Generator, List, Tuple, Callable, Optional, Match


spec: List[Tuple[str, str]] = [
    ('NUM', r'\d+(?:[\.,]\d+)?'),
    ('ID', r'[A-Za-z]+\d*'),
    ('ATRIB_ADD', r'\+='),
    ('ATRIB_SUB', r'-='),
    ('ATRIB', r'='),
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
    ('ELSE', r'else'),
    ('VAR', r'var'),
    ('FOR', r'for'),
    ('WHILE', r'while'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('COMMA', r','),
    ('SEMICOLON', r';'),
    ('INT', r'int'),
    ('REAL', r'real'),
    ('STR', r'str'),
    ('BOOL', r'bool'),
    ('UNKNOWN', r'[^ \n\t]+'),
]


def lexicon(code: str) -> Generator[str, None, None]:
    tok: str = '|'.join('(?P<%s>%s)' % pair for pair in spec)
    get_token: Callable[[str, int, int], Optional[Match[str]]] = re.compile(tok).match

    pos: int = 0
    val: Optional[Match[str]] = get_token(code, pos)

    while val is not None:
        token: Optional[str] = val.lastgroup
        lexeme: Optional[str] = val.group()
        if token != 'SKIP':
            if token == 'ID' and lexeme.strip() in ['if', 'else', 'while', 'var', 'int', 'real', 'for', 'str', 'bool']:
                token = lexeme.strip().upper()
            elif token == 'ATRIB':
                next_char = code[val.end():val.end() + 1]
                if next_char == '+':
                    token = 'ATRIB_ADD'
                elif next_char == '-':
                    token = 'ATRIB_SUB'
            yield ('TOKEN: %s\t VAL: %s' % (token, lexeme))
        pos = val.end() if val is not None else pos + 1
        val = get_token(code, pos)


def read_code(file_name: str) -> str:
    with open(file_name, 'r') as file:
        code = file.read()
    return code


def analyze_code(file_name: str) -> None:
    code = read_code(file_name)
    for token in lexicon(code):
        print(token)


def verify_tokens(file_name: str) -> bool:
    with open(file_name, 'r') as file:
        code = file.read()

    tok: str = '|'.join('(?P<%s>%s)' % pair for pair in spec)
    get_token: Callable[[str, int, int], Optional[Match[str]]] = re.compile(tok).match

    pos: int = 0
    val: Optional[Match[str]] = get_token(code, pos)

    var_found = False
    while val is not None:
        token = val.lastgroup

        if token == 'UNKNOWN':
            return False
        elif token == 'VAR':
            var_found = True

        pos = val.end()
        val = get_token(code, pos)

    if var_found:
        return re.search(r'\bvar\b', code) is not None

    return True


def get_tokens_code(file_name: str):
    code = read_code(file_name)
    tokens = []
    lexemas = []

    for token in lexicon(code):
        token_parts = token.split('\t')
        if len(token_parts) >= 2:
            token_name = token_parts[0].split(':')[1].strip()
            tokens.append(token_name.split(':')[0].strip())
            lexema_name = token_parts[1].split(':')[1].strip()
            lexemas.append(lexema_name.split(':')[0].strip())
    return tokens, lexemas


if __name__ == '__main__':
#    analyze_code('codigo2.txt')
    tokens, lexemas = get_tokens_code('codigo2.txt')
#    print(check_different_tokens := verify_tokens('codigo2.txt'))
