from typing import List
from lexer import lexicon_from_file

def parsin(tokens):
    token_index: int = 0
    token_count: int = len(tokens)
    token_key = list(((key, value) for key, value in tokens[token_index].items()))
    errors: List[str] = []
    matchs: List[str] = []
    last_temp = token_key
    e1 = 0
    e2 = 0
    e3 = 0

    def match(expected_token: str) -> None:
        nonlocal token_index, token_key
        if token_key[0][0] == expected_token:
            token_index += 1
            if token_index < token_count:
                token_key = list(((key, value) for key, value in tokens
    [token_index].items()))
            else:
                token = None
        else:
            errors.append(f"Expected '{expected_token}', but found '{token_key[0][1]}'")


    def check_if() -> None:
        nonlocal last_temp,e1, e2, e3
        match('IF')
        matchs.append('IF ok')
        if token_key[0][0] == 'LPAREN':
            match('LPAREN')
            matchs.append('LPAREN ok')
            if token_key[0][0] == 'ID' or token_key[0][0] == 'NUM':
                e1 = token_key[0][0]
                match(token_key[0][0])
                
                e2 = check_relational_expressions()
                
                if token_key[0][0] == 'RPAREN':
                        match('RPAREN')
                        matchs.append('RPAREN ok')
                        if token_key[0][0] == 'LBRACE':
                            matchs.append('LBRACE ok')
                            match('LBRACE')
                            #check_id()
                            if token_key[0][0] == 'RBRACE':
                                matchs.append('RBRACE  ok')
                                if token_index + 1 < token_count:
                                    match('RBRACE')
                                    #analyze_list(token_key[0][0])
                            else:
                                errors.append(
                                    f'Expected "}}", but received {token_key[0][1]}')
                        else:
                            errors.append(f'Expected "{{", but received {token_key[0][1]}')
                else:
                    errors.append(f'Expected ")", but received {token_key[0][1]}')
        else:
            errors.append(f'Expected "(", but received {token_key[0][1]}')


    if token_key[0][0] == 'IF':
        check_if()

    exp = f'{e1} {e2} {e3}' 
    t1 = f'{token_key[0][0]}false {exp} goto {last_temp}' 


    def check_relational_expressions():
        if token_key[0][0] in ['LT', 'GT', 'LTE', 'GTE', 'EQ', 'ATRIB_ADD', 'ATRIB_SUB']:
            matchs.append('Relational expressions ok')
            temp = token_key[0][0]
            match(token_key[0][0])
            return temp
        else:
            errors.append(f'Expected a relational expressions, but received {token_key[0][1]}')



token_symbols = list(lexicon_from_file('codigo2.txt'))
parsin(token_symbols)