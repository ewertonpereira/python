from typing import List
from lexer import verify_tokens, get_tokens_code, lexicon_from_file


def analyze_code_with_verification(file_name: str, show_errors: bool = True) -> bool:
    if verify_tokens(file_name):
        print("Verificação de tokens bem-sucedida.\nComeçaremos o processo de análise sintática. Por favor, aguarde...")
        return True
    return False
    

def parser(tokens) ->  list[str]:
    token_index: int = 0
    token_count: int = len(tokens)
    
    token_key = list(((key, value) for key, value in tokens
    [token_index].items()))
    errors: List[str] = []
    matchs: List[str] = []

    
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
            

    def analyze_list(token: str) -> None:
        actions = {
            'VAR': check_var,
            'ID': check_id,
            'WHILE': check_while,
            'IF': check_if,
            'ELSE': check_else,
            'RBRACE': lambda: token,
        }

        if token_key[0][0] in actions:
            actions[token_key[0][0]]()
        else:
            errors.append(f'Variável inválida: {token}')
        

    def check_id():
        if token_key[0][0] == 'ID':
            match('ID')
            matchs.append('ID ok')
            if token_key[0][0] == 'COMMA':
                match('COMMA')
                check_id()
            elif token_key[0][0] == 'ATRIB':
                match('ATRIB')
                matchs.append('ATRIB ok')
                if token_key[0][0] == 'LPAREN':
                    check_arithmetic_expressions()
                elif token_key[0][0] == 'ID' or token_key[0][0] == 'NUM':
                    match(token_key[0][0])
                    check_basic_arithmetic_expressions()
                    if token_key[0][0] == 'NUM':
                        check_num()
                    if token_key[0][0] == 'ID':
                        check_id()
                else:
                    errors.append(f'"ATRIB" expected a variable, but received {token_key[0][1]}')
            elif token_key[0][0] in ['LT', 'GT', 'LTE', 'GTE', 'EQ']:
                match(token_key[0][0])               
                if token_key[0][0] == 'ID' or token_key[0][0] == 'NUM':
                    matchs.append('Relational expressions ok')
                    match(token_key[0][0])
                else:
                    errors.append(f"Relational expressions expected a variable, but received {token_key[0][1]}")
                    exit()      
            elif token_key[0][0] in ['ADD', 'SUB', 'MUL', 'DIV', 'POW']:
                match(token_key[0][0])
                if token_key[0][0] == 'ID' or token_key[0][0] == 'NUM':
                    matchs.append('Arithmetic expressions ok')
                    match(token_key[0][0])
                else:
                    errors.append(f"Arithmetic expressions expected a variable, but received {token_key[0][1]}")
            elif token_key[0][0] == 'RPAREN':
                check_arithmetic_expressions()
            elif token_key[0][0] in ['ATRIB_ADD', 'ATRIB_SUB']:
                matchs.append('combined assignment operator ok')
                match(token_key[0][0])
                if token_key[0][0] == 'ID':
                    check_id()
                elif token_key[0][0] == 'NUM':
                    check_num()
                else:
                    errors.append(f'Expected "ID" or "NUM", but received {token_key[0][1]}'   )
            if token_key[0][0] == 'SEMICOLON':
                check_semicolon()
                return True
            else:
                return False
        else:
            errors.append(f'Expected "ID", but received {token_key[0][1]}')
            

    def check_semicolon() -> None:
        matchs.append('SEMICOLON ok')
        match('SEMICOLON')
        if token_index >= token_count:
            print('Fim do código')
            
            
    def check_while() -> bool:
        match('WHILE')
        matchs.append('WHILE ok')
        if token_key[0][0] == 'LPAREN':
            match('LPAREN')
            matchs.append('LPAREN ok')
            if token_key[0][0] == 'ID':
                check_id()
                if token_key[0][0] == 'RPAREN':
                    match('RPAREN')
                    matchs.append('RPAREN ok')
                    if token_key[0][0] == 'LBRACE':
                        match('LBRACE')
                        matchs.append('LBRACE ok')
                        if token_key[0][0] == 'ID':
                            check_id()
                            if token_key[0][0] == 'IF':
                                check_if()
                                analyze_list(token_key[0][0])
                                if token_key[0][0] == 'ELSE':
                                    check_else()
                                analyze_list(token_key[0][0])
                        if token_key[0][0] == 'RBRACE':
                            matchs.append('RBRACE WHILE ok')
                            if token_index + 1 < token_count:
                                match('RBRACE')
                            analyze_list(token_key[0][0])                          
                else:
                    errors.append(
                        f'Expected "ID" or ")", but received {token_key[0][1]}')
            else:
                errors.append(
                    f'Expected "ID" or ")", but received {token_key[0][1]}')
        return True


    def check_if() -> None:
        match('IF')
        matchs.append('IF ok')
        if token_key[0][0] == 'LPAREN':
            match('LPAREN')
            matchs.append('LPAREN ok')
            check_id()
            if token_key[0][0] == 'RPAREN':
                match('RPAREN')
                matchs.append('RPAREN ok')
                if token_key[0][0] == 'LBRACE':
                    matchs.append('LBRACE ok')
                    match('LBRACE')
                    check_id()
                    if token_key[0][0] == 'RBRACE':
                        matchs.append('RBRACE  ok')
                        if token_index + 1 < token_count:
                            match('RBRACE')
                            analyze_list(token_key[0][0])
                    else:
                        errors.append(
                            f'Expected "}}", but received {token_key[0][1]}')
                else:
                    errors.append(f'Expected "{{", but received {token_key[0][1]}')
            else:
                errors.append(f'Expected ")", but received {token_key[0][1]}')
        else:
            errors.append(f'Expected "(", but received {token_key[0][1]}')


    def check_else() -> None:
        match('ELSE')
        matchs.append('ELSE ok')
        if token_key[0][0] == 'LBRACE':
            match('LBRACE')
            matchs.append('LBRACE ok')
            check_id()
            if token_key[0][0] == 'RBRACE':
                matchs.append('RBRACE ELSE ok')
                if token_index + 1 < token_count:
                    match('RBRACE')
                    analyze_list(token_key[0][0])
            else:
                errors.append(f'Expected "}}", but received {token_key[0][1]}')
        else:
            errors.append(f'Expected "{{", but received {token_key[0][1]}')


    def check_num() -> None:
        match('NUM')
        matchs.append('NUM ok')
        check_basic_arithmetic_expressions()
        check_relational_expressions()
        

    def check_basic_arithmetic_expressions() -> None:
        if token_key[0][0] in ['ADD', 'SUB', 'MUL', 'DIV']:
            match(token_key[0][0])
            matchs.append('Expressões aritméticas ok')
        elif token_key[0][0] == 'POW':
            match('POW')
            if token_key[0][0] == 'ID' or token_key[0][0] == 'NUM':
                match(token_key[0][0])
                check_basic_arithmetic_expressions()

    
    def check_arithmetic_expressions() -> None:
        if token_key[0][0] == 'LPAREN':
            match('LPAREN')
            matchs.append('LPAREN ok')
            check_arithmetic_expressions()
            if token_key[0][0] == 'RPAREN':
                match('RPAREN')
                matchs.append('RPAREN CLOSED ok')
                if token_index + 1 < token_count:
                    check_basic_arithmetic_expressions()
                    check_arithmetic_expressions()
            else:
                errors.append(f'Expected ")", but received {token_key[0][1]}')
        elif token_key[0][0] == 'NUM':
            matchs.append('NUM ok')
            match('NUM')
            check_basic_arithmetic_expressions()
            check_arithmetic_expressions()
        elif token_key[0][0] == 'ID':
            check_id()
        elif token_key[0][0] == 'LPAREN':
            matchs.append('LPAREN ok')


    def check_relational_expressions() -> None:
        if token_key[0][0] in ['LT', 'GT', 'LTE', 'GTE', 'EQ']:
            matchs.append('Relational expressions ok')
            match(token_key[0][0])


    def check_var() -> None:
        match('VAR')
        matchs.append('VAR ok')
        if token_key[0][0] in ['INT', 'STR', 'REAL', 'BOOL']:
            match(token_key[0][0])
            check_id()


    def show_list_checks() -> None:
        print('========== START ==========')
        for item in matchs:
            print(item)
        print('=========== END ===========')


    while token_index < token_count:
        if token_key[0][0] == None:
            break
        elif token_key[0][0] == 'ID':
            check_id()
        elif token_key[0][0] == 'VAR':
            check_var()
        elif token_key[0][0] == 'IF':
            check_if()
        elif token_key[0][0] == 'ELSE':
            check_else()
        elif token_key[0][0] == 'WHILE':
            check_while()
        elif token_key[0][0] not in ['VAR', 'ID', 'IF', 'WHILE']:
            if not matchs:
                errors.append(f"This token can not start a sentence: {token_key[0][1]}")
            break
        else:
            errors.append(f"Invalid token: {token_key[0][1]}")
        

    if matchs:
        show_list_checks()

    return errors


def analyze_code(file_name: str) -> None:
    if analyze_code_with_verification(file_name):
        #token_symbols = get_tokens_code(file_name)
        token_symbols = list(lexicon_from_file(file_name))
        # print(token_symbols)
        errors = parser(token_symbols)
        if not errors:
            success_message = "Análise sintática bem-sucedida!"
            return print(success_message)
        else:
            error_message = "\nErros encontrados durante a análise sintática:"
            return print(error_message, errors)
    else:
        verification_error_message = "Erro na verificação dos tokens. Verifique o arquivo selecionado e tente novamente."
        return print(verification_error_message)


analyze_code('codigo2.txt')
