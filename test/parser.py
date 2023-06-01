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


def read_token_values(file_name: str) -> List[str]:
    with open(file_name, 'r') as file:
        code = file.read().split()

    return code


def parser(tokens: List[str]) -> dict:
    token_index = 0
    token_count = len(tokens)
    token = tokens[token_index]
    errors = []

    def match(expected_token):
        nonlocal token, token_index
        if token == expected_token:
            token_index += 1
            if token_index < token_count:
                token = tokens[token_index]
            else:
                token = None
        else:
            raise SyntaxError(
                f"Expected '{expected_token}', but found '{token}'")

    def EXP():
        nonlocal token
        if TERM():
            if EXPL():
                return True
        return False

    def EXPL():
        nonlocal token
        if token in ['+', '-']:
            match(token)
            if TERM():
                if EXPL():
                    return True
            else:
                return False
        return True

    def TERM():
        nonlocal token
        if FATOR():
            return True
        return False

    def check_var():
        match('VAR')
        if token in ['INT', 'REAL', 'STR', 'BOOL']:
            match(token)
            print('VAR ok')
            check_id()
            return True
        else:
            errors.append(
                "Expected one of ['int', 'real', 'str', 'bool'] after 'var' declaration")
            return False

    def check_id():
        match('ID')
        print('ID ok')
        if token == 'COMMA':
            match(token)
            check_id()

        elif token == 'ATRIB':
            match('ATRIB')
            print('ATRIB ok')
            if token == 'ID' or token == 'NUM':
                match(token)
                print(token) #
                check_basic_arithmetic_expressions(token)
                if token == 'NUM':
                    check_num()

                print('galinha assada')
                print(token)
            else:
                errors.append(
                    f'"ATRIB" expected a variable, but received {token}')

        elif token in ['LT', 'GT', 'LTE', 'GTE', 'EQ']:
            match(token)
            if token == 'ID' or token == 'NUM':
                print('Relational expressions ok')
                match(token)
            else:
                errors.append(f"Relational expressions expected a variable, but received {token}")
            
        elif token in ['ADD', 'SUB', 'MUL', 'DIV', 'POW']: 
            match(token)
            if token == 'ID' or token == 'NUM':
                print('Arithmetic expressions ok')
                match(token)
            else:
                errors.append(f"Arithmetic expressions expected a variable, but received {token}")

        if token == 'SEMICOLON':
            check_semicolon()

            print('Token atual:', token)
            return True
        else:
            errors.append(f"Variable COMMA or ATRIB {token}")
            return False

    def check_semicolon():
        print('SEMICOLON ok')
        match('SEMICOLON')
        print(token)


    def check_while():
        match('WHILE')
        print('WHILE ok')
        if token == 'LPAREN':
            match('LPAREN')
            print('LPAREN ok')
            if token == 'ID':
                check_id()
                print(token)
                if token == 'RPAREN':
                    match('RPAREN')
                    print('RPAREN ok')

                    if token == 'LBRACE':
                        match('LBRACE')
                        print('LBRACE ok')
                        # if token == 'ID':
                        #     check_id()
                        #     if token == 'IF':
                        #         check_if()
                        #         if token == 'ELSE':
                        #             check_else()
                        #             if token == 'ID':
                        #                 print('bola amarela')

                    
                    if token == 'RBRACE':
                        print('RBRACE while ok')

                else:
                    errors.append(f'Expected "ID" or "RPAREN", but received {token}')

            # if token == 'NUM':
            #     check_num()
            #     print(token)
            #     if token == 'IF':
            #         check_if()
            #         if token == 'ELSE':
            #             check_else()
            
            #             if token == 'RBRACE':
            #                 print('RBRACE while ok')
                            
            # else:
            #     errors.append(f'Expected "boi or NUM", but received {token}')

        
        else:
            errors.append(f'Expected "LPAREN", but received {token}')

    def check_if():
        match('IF')
        print('IF ok')
        if token == 'LPAREN':
            match('LPAREN')
            print('LPAREN ok')
            check_id()
            if token == 'RPAREN':
                match('RPAREN')
                print('RPAREN ok')
                if token == 'LBRACE':
                    print('LBRACE ok')
                    match('LBRACE')
                    check_id()
                    check_id()
                    if token == 'RBRACE':
                        print('RBRACE if ok')
                        match('RBRACE') 
                        print(token)
                    else:
                        errors.append(f'Expected "RBRACE", but received {token}')
                else:
                    errors.append(f'Expected "LBRACE", but received {token}')
            else:
                errors.append(f'Expected "RPAREN", but received {token}')
        else:
            errors.append(f'Expected "LPAREN", but received {token}')


    def check_else():
        match('ELSE')
        print('ELSE ok')
        if token == 'LBRACE':
            print('LBRACE ok')
            match('LBRACE')
            check_id()
            if token == 'RBRACE':
                print('RBRACE else ok')
                match('RBRACE')
            else:
                errors.append(f'Expected "RBRACE", but received {token}')
        else:
            errors.append(f'Expected "LBRACE", but received {token}')       

    def check_num():
        match('NUM')
        print('NUM ok')
        check_basic_arithmetic_expressions(token)

        check_relational_expressions(token)
        print(token)

    
    def check_basic_arithmetic_expressions(token):
        if token in ['ADD', 'SUB', 'MUL', 'DIV']:
            print('Expressões aritméticas ok')
            match(token)
            if token == 'ID' or token == 'NUM':
                print('agora bombou maaaaané')
                match(token)
        elif token == 'POW':
            match('POW')
            if token == 'ID' or token == 'NUM':
                check_basic_arithmetic_expressions(token)


    def check_relational_expressions(token):
        if token in ['LT', 'GT', 'LTE', 'GTE', 'EQ']:
            print('Relational expressions ok')
            match(token)


    def FATOR():
        nonlocal token

        cases = {
            'VAR': check_var,
            'ID': check_id,
            'WHILE': check_while,
            'IF': check_if,
            'ELSE': check_else,
            #'NUM': check_num,
            #'SEMICOLON': check_semicolon,
        }

        if token in cases:
            while token in cases:
                cases[token]()
            return True
        else:
            return False

    try:
        if EXP() and token is None:
            return {'success': True, 'errors': errors}
        else:
            return {'success': False, 'errors': errors}
    except SyntaxError as e:
        errors.append(str(e))
        return {'success': False, 'errors': errors}


def process_code_file(file_name: str) -> None:
    if analyze_code_with_verification(file_name):
        token_symbols = get_tokens_code(file_name)
        result = parser(token_symbols)
        # print(token_symbols)
        if result['success']:
            print("Análise sintática concluída. Gramática válida.")
        else:
            print("Análise sintática concluída. Gramática inválida.")
            print("Erros encontrados:")
            for error in result['errors']:
                print(f"- {error}")

    else:
        print("Erro: O código não está de acordo com a gramática especificada.")


process_code_file('codigo.txt')
