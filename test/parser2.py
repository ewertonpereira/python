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

    # def TERML():
    #     nonlocal token
    #     if token in ['*', '/']:
    #         match(token)
    #         if FATOR():
    #             if TERML():
    #                 return True
    #     return True

    def check_var():
        match('VAR')
        if token in ['INT', 'REAL', 'STR', 'BOOL']:
            match(token)

            if token == 'ID':
                match('ID')

                if token == 'COMMA':
                    match('COMMA')

                    if token == 'ID':
                        match('ID')
                        if token == 'SEMICOLON':
                            match('SEMICOLON')
                        else:
                            errors.append("Variable name expected after semicolon")
                            return False
                    else:
                        errors.append("Variable name expected after comma")
                        return False
            print('Token atual:', token)
            print('ok')
            return True
        else:
            errors.append(
                "Expected one of ['int', 'real', 'str', 'bool'] after 'var' declaration")
            return False
        

    def check_id():
        print('Token atual:', token)  # Adicione esta linha
        match('ID')
        if token == 'ATRIB':
            match('ATRIB')

            if token in ['INT', 'REAL', 'STR', 'BOOL', 'NUM']:
                match(token)

                if token == 'SEMICOLON':
                    match('SEMICOLON')
                else:
                    errors.append("Variable name expected after semicolon")
                    return False
            else:
                print('ooooo')
            print('ok')
            return True  # Adicione esta linha
        else:
            errors.append("Variable ATRIB")
            return False


    def FATOR():
        nonlocal token

        cases = {
            'VAR': check_var,
            'ID': check_id,
            # Adicione outros casos conforme necessário
        }
        if token in cases:
            while token in cases:
                cases[token]()
            return True
        else:
            return False  


    '''def check_while():
        match('WHILE')
        if token == 'COLON':
            print('aiaiaia')
            match('COLON')
                
            while token != 'ENDWHILE':
                if not check_statement():
                    return False
            match('ENDWHILE')
            return True
        else:
            errors.append("Missing colon after while condition")
            return False
        

    def check_statement():
        if token == 'ID':
            match('ID')
            if token == 'SEMICOLON':
                match('SEMICOLON')
                return True
            else:
                errors.append("Missing semicolon after statement")
                return False
        else:
            errors.append("Invalid statement")
            return False
'''

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
