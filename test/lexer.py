import re
from typing import Generator, List, Tuple, Callable, Optional, Match


def lexicon(code: str) -> Generator[str, None, None]:
    spec: List[Tuple[str, str]] = [
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
        ('FOR', r'for'),
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
        ('UNKNOWN', r'.'),
    ]

    tok: str = '|'.join('(?P<%s>%s)' % pair for pair in spec)
    get_token: Callable[[str, int, int], Optional[Match[str]]] = re.compile(tok).match

    pos: int = 0
    val: Optional[Match[str]] = get_token(code, pos)

    while val is not None:
        token: Optional[str] = val.lastgroup
        lexeme: Optional[str] = val.group()
        if token != 'SKIP':
            if token == 'ID' and lexeme.strip() in ['if', 'while', 'var', 'int', 'real, for']:
                token = lexeme.strip().upper()
            elif token == 'ID':
                if re.match(r'^[A-Za-z]+$', lexeme):
                    token = 'ID_VAR'
                else:
                    token = 'ID'
            yield ('TOKEN: %s\t VAL: %s' % (token, lexeme))
        pos = val.end()
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

    spec: List[Tuple[str, str]] = [
        ('UNKNOWN', r'.'),
    ]

    tok: str = '|'.join('(?P<%s>%s)' % pair for pair in spec)
    get_token: Callable[[str, int, int], Optional[Match[str]]] = re.compile(tok).match

    pos: int = 0
    val: Optional[Match[str]] = get_token(code, pos)

    while val is not None:
        token = val.lastgroup

        if token == 'UNKNOWN':
            return False

        pos = val.end()
        val = get_token(code, pos)

    return True


if __name__ == '__main__':
    analyze_code('codigo.txt')
    print(check_different_tokens := verify_tokens('codigo.txt'))
