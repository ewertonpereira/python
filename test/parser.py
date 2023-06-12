from typing import List
from lexer import verify_tokens, get_tokens_code


def analyze_code_with_verification(file_name, show_errors=True):
    if verify_tokens(file_name):
        print("Verificação de tokens bem-sucedida.\nComeçaremos o processo de análise sintática. Por favor, aguarde...")
        return True
    else:
        error_message = "Erro: Token inválido encontrado.\nVerifique o arquivo selecionado e tente novamente."
        print(error_message) if show_errors else None
        return False


def parser(tokens: List[str]):
    token_index = 0
    token_count = len(tokens)
    token = tokens[token_index]
    errors = []
    matchs = []
    
    def match(expected_token):
        nonlocal token, token_index
        if token == expected_token:
            token_index += 1
            if token_index < token_count:
                token = tokens[token_index]
            else:
                token = None
        else:
            errors.append(f"Expected '{expected_token}', but found '{token}'")
            

    def analyze_list(token):
        actions = {
            'VAR': check_var,
            'ID': check_id,
            'WHILE': check_while,
            'IF': check_if,
            'ELSE': check_else,
            'RBRACE': lambda: token,
        }

        if token in actions:
            actions[token]()
        else:
            errors.append(f'Variável inválida: {token}')
        

    def check_id():
        if token == 'ID':
            match('ID')
            matchs.append('ID ok')
            if token == 'COMMA':
                match('COMMA')
                check_id()
            elif token == 'ATRIB':
                match('ATRIB')
                matchs.append('ATRIB ok')
                if token == 'ID' or token == 'NUM':
                    match(token)
                    check_basic_arithmetic_expressions(token)
                    if token == 'NUM':
                        check_num()
                    if token == 'ID':
                        check_id()
                else:
                    errors.append(f'"ATRIB" expected a variable, but received {token}')
            elif token in ['LT', 'GT', 'LTE', 'GTE', 'EQ']:
                match(token)
                if token == 'ID' or token == 'NUM':
                    matchs.append('Relational expressions ok')
                    match(token)
                else:
                    errors.append(f"Relational expressions expected a variable, but received {token}")
                    print(errors)
                    exit()      
            elif token in ['ADD', 'SUB', 'MUL', 'DIV', 'POW']:
                match(token)
                if token == 'ID' or token == 'NUM':
                    matchs.append('Arithmetic expressions ok')
                    match(token)
                else:
                    errors.append(f"Arithmetic expressions expected a variable, but received {token}")
            elif token == 'RPAREN':
                check_arithmetic_expressions()
            elif token in ['ATRIB_ADD', 'ATRIB_SUB']:
                matchs.append('combined assignment operator ok')
                match(token)
                if token == 'ID':
                    check_id()
                elif token == 'NUM':
                    check_num()
            if token == 'SEMICOLON':
                check_semicolon()
                return True
            else:
                return False
        else:
            errors.append(f'Expected "ID", but received {token}')

            
    def check_semicolon():
        matchs.append('SEMICOLON ok')
        if token_index + 1 < token_count:
            match('SEMICOLON')
        else:
            print('Fim do código')
            
            
    def check_while():
        match('WHILE')
        matchs.append('WHILE ok')
        if token == 'LPAREN':
            match('LPAREN')
            matchs.append('LPAREN ok')
            if token == 'ID':
                check_id()
                if token == 'RPAREN':
                    match('RPAREN')
                    matchs.append('RPAREN ok')
                    if token == 'LBRACE':
                        match('LBRACE')
                        matchs.append('LBRACE ok')
                        if token == 'ID':
                            check_id()
                            if token == 'IF':
                                check_if()
                                analyze_list(token)
                                if token == 'ELSE':
                                    check_else()
                                analyze_list(token)
                        if token == 'RBRACE':
                            matchs.append('RBRACE WHILE ok')
                            if token_index + 1 < token_count:
                                match('RBRACE')
                            analyze_list(token)                          
                else:
                    errors.append(
                        f'Expected "ID" or "RPAREN 1", but received {token}')
            else:
                errors.append(
                    f'Expected "ID" or "RPAREN" 2, but received {token}')
        return True


    def check_if():
        match('IF')
        matchs.append('IF ok')
        if token == 'LPAREN':
            match('LPAREN')
            matchs.append('LPAREN ok')
            check_id()
            if token == 'RPAREN':
                match('RPAREN')
                matchs.append('RPAREN ok')
                if token == 'LBRACE':
                    matchs.append('LBRACE ok')
                    match('LBRACE')
                    check_id()
                    if token == 'RBRACE':
                        matchs.append('RBRACE  ok')
                        if token_index + 1 < token_count:
                            match('RBRACE')
                            analyze_list(token)
                    else:
                        errors.append(
                            f'Expected "RBRACE", but received {token}')
                else:
                    errors.append(f'Expected "LBRACE", but received {token}')
            else:
                errors.append(f'Expected "RPAREN", but received {token}')
        else:
            errors.append(f'Expected "LPAREN", but received {token}')


    def check_else():
        match('ELSE')
        matchs.append('ELSE ok')
        if token == 'LBRACE':
            match('LBRACE')
            matchs.append('LBRACE ok')
            check_id()
            if token == 'RBRACE':
                matchs.append('RBRACE ELSE ok')
                if token_index + 1 < token_count:
                    match('RBRACE')
                    analyze_list(token)
            else:
                errors.append(f'Expected "RBRACE", but received {token}')
        else:
            errors.append(f'Expected "LBRACE", but received {token}')


    def check_num():
        match('NUM')
        matchs.append('NUM ok')
        check_basic_arithmetic_expressions(token)
        check_relational_expressions(token)
        

    def check_basic_arithmetic_expressions(token):
        if token in ['ADD', 'SUB', 'MUL', 'DIV']:
            match(token)
            matchs.append('Expressões aritméticas ok')
            print('Expressões aritméticas ok') ###########
        elif token == 'POW':
            match('POW')
            if token == 'ID' or token == 'NUM':
                check_basic_arithmetic_expressions(token)

    ##################################
    def check_arithmetic_expressions():
        if token == 'LPAREN':
            match('LPAREN')
            print('LPAREN ok')
            check_arithmetic_expressions()
            if token == 'RPAREN':
                match('RPAREN')
                print('RPAREN CLOSED ok')
                if token_index + 1 < token_count:
                    check_basic_arithmetic_expressions(token)
                    check_arithmetic_expressions()
            else:
                errors.append(f'Expected "RPAREN", but received {token}')
        elif token == 'NUM':
            print('NUM ok')
            match('NUM')
            print(token)
            check_basic_arithmetic_expressions(token)
            print(token)
            check_arithmetic_expressions()
        elif token == 'ID':
            check_id()
        elif token == 'LPAREN':
            print('LPAREN ok')
            


    def check_relational_expressions(token):
        if token in ['LT', 'GT', 'LTE', 'GTE', 'EQ']:
            matchs.append('Relational expressions ok')
            match(token)


    def check_var():
        match('VAR')
        matchs.append('VAR ok')
        if token in ['INT', 'STR', 'REAL', 'BOOL']:
            match(token)
            check_id()


    def show_list_checks():
        print('========== CHECK IN ===========')
        for item in matchs:
            print(item)
        print('========= CHECK OUT ===========')


    while token_index < token_count:
        if token == 'SEMICOLON':
            break
        elif token == 'ID':
            check_id()
        elif token == 'VAR':
            check_var()
        elif token == 'IF':
            check_if()
        elif token == 'ELSE':
            check_else()
        elif token == 'WHILE':
            check_while()
        elif token == 'LPAREN':
            check_arithmetic_expressions()
        else:
            errors.append(f"Invalid token: {token}")
        

    show_list_checks()
    return errors


def analyze_code(file_name: str):
    if analyze_code_with_verification(file_name):
        token_symbols = get_tokens_code(file_name)
        print(token_symbols)
        errors = parser(token_symbols)
        if not errors:
            success_message = "Análise sintática bem-sucedida!"
            return print(success_message)
        else:
            error_message = "Erros encontrados durante a análise sintática:"
            return print(error_message, errors)
    else:
        verification_error_message = "Erro na verificação dos tokens. Verifique o arquivo selecionado e tente novamente."
        return print(verification_error_message, [])


analyze_code('codigo2.txt')
