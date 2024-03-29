from typing import List
from lexer import verify_tokens, get_tokens_code


def analyze_code_with_verification(file_name: str) -> bool:
    if verify_tokens(file_name):
        print("Verificação de tokens bem-sucedida.\nComeçaremos o processo de análise sintática. Por favor, aguarde...")
        return True
    return False


def parser(tokens: List[str], lexemas: List[str]):
    token_index: int = 0
    token_count: int = len(tokens)
    token: str = tokens[token_index]
    errors: List[str] = []
    matchs: List[str] = []
    cont = -1
    contLabel = -1


    def geraTemp():
        nonlocal cont
        cont += 1
        return ("T"+str(cont))


    def geraLabel():
        nonlocal contLabel
        contLabel += 1
        return ("L"+str(contLabel))


    def geraCod(linhaCod):
        print(linhaCod)


    def match(expected_token: str) :
        nonlocal token, token_index
        lexema = ''
        if token == expected_token:
            lexema = lexemas[token_index]
            token_index += 1
            if token_index < token_count:
                token = tokens[token_index]
        else:
            errors.append(f"Expected '{expected_token}', but found '{token}'")
        return lexema


    def analyze_list(token: str) -> None:
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


    relTEMP = ''
    lexOPREL = ''
    last_label = ''
    last_go_to= ''
    lexARI = ''
    lexARI_RIGHT = ''
    aft_comma = ''
    def check_id():
        nonlocal relTEMP, ifTRUE, ifFALSE, lmark, last_token, lexOPREL, last_label, ifmark, last_go_to, lexARI, lexARI_RIGHT, aft_comma

        lexEXP_RIGHT = ''
        
        if token == 'ID':
            lexID = match('ID')
            matchs.append('ID ok')
            if token == 'COMMA':
                match('COMMA')
                aft_comma = check_id()
            elif token == 'ATRIB':
                match('ATRIB')
                matchs.append('ATRIB ok')
                if token == 'LPAREN':
                    check_arithmetic_expressions()
                elif token == 'ID' or token == 'NUM':
                    lexEXP_LEFT = match(token)
                    lexOPA = check_basic_arithmetic_expressions()

                    if token == 'NUM':
                        lexEXP_RIGHT = check_num()

                    if token == 'ID':
                        lexEXP_RIGHT = check_id()
                    
                    if last_token in ['IF', 'ELSE', 'WHILE']:
                        # if ifFALSE == 'L0':
                        #     geraCod(ifFALSE+' :')
                        if last_token == 'WHILE':
                            geraCod(whilemark+' :')
                        elif last_token == 'IF':
                            geraCod(last_go_to+' :')
                        elif last_token == 'ELSE':
                            geraCod(ifmark+' :')
                            lmark = geraLabel()
                            last_token = 'LABEL'
                        elif last_token == 'LABEL':
                            pass
                            # geraCod(last_label+' :') # type: ignore
                        else:
                            geraCod(lmark+' :')
                            lmark = geraLabel()
                

                    relTEMP = geraTemp()

                    if lexOPA:
                        if lexARI:
                            relTEMP = geraTemp()
                            geraCod(relTEMP+' = '+lexEXP_RIGHT+lexARI+lexARI_RIGHT) # type: ignore
                            lexARI = False
                            lexARI_temp = relTEMP
                            relTEMP = geraTemp()
                            geraCod(relTEMP+ ' = '+lexEXP_LEFT+lexOPA+lexARI_temp)# type: ignore

                        else:
                            geraCod(relTEMP+ ' = '+lexEXP_LEFT+lexOPA+lexEXP_RIGHT)# type: ignore
                    else: 
                        geraCod(relTEMP+ ' = '+lexEXP_LEFT) # type: ignore
                    geraCod(lexID+' = '+relTEMP) # type: ignore
                    ifTRUE = geraLabel()
                    
                    if lexOPREL:
                        if last_token != 'WHILE' and last_token != 'IF' and last_token != 'LABEL':

                            geraCod('goto '+ifTRUE+' :')# type: ignore
                            last_go_to = ifTRUE
                            lexOPREL = False
                            if last_token == 'IF':
                                last_label = ifTRUE
                        
                    ifFALSE = ifTRUE
                    relTEMP = ifTRUE
                    print(' ')
                else:
                    errors.append(
                        f'"ATRIB" expected a variable, but received {token}')
            elif token in ['LT', 'GT', 'LTE', 'GTE', 'EQ']:
                lexOPREL = match(token)
                if token == 'ID' or token == 'NUM':
                    matchs.append('Relational expressions ok')
                    lexRIGHT = match(token)
                   
                    relTEMP = geraTemp()
                    geraCod(relTEMP+' = '+lexID+lexOPREL+lexRIGHT) # type: ignore
                    return relTEMP
                else:
                    errors.append(
                        f"Relational expressions expected a variable, but received {token}")
                    exit()
            elif token in ['ADD', 'SUB', 'MUL', 'DIV', 'POW']:
                lexARI = match(token)
                if token == 'ID' or token == 'NUM':
                    matchs.append('Arithmetic expressions ok')
                    lexARI_RIGHT = match(token)
                else:
                    errors.append(
                        f"Arithmetic expressions expected a variable, but received {token}")
            elif token == 'RPAREN':
                check_arithmetic_expressions()
            elif token in ['ATRIB_ADD', 'ATRIB_SUB']:
                lexOPA = combined_assignment_operator()
                

                if token == 'ID' or token == 'NUM':
                    if token == 'ID':
                        lexEXP_RIGHT = check_id()
                    if token == 'NUM':
                        lexEXP_RIGHT = check_num()

                    relTEMP = geraTemp()
                    geraCod(relTEMP+ ' = '+lexID+lexOPA+lexEXP_RIGHT)# type: ignore
                    geraCod(lexID+' = '+relTEMP)# type: ignore
            
                else:
                    errors.append(
                        f'Expected "ID" or "NUM", but received {token}')
            if token == 'SEMICOLON':
                check_semicolon()
                return lexID
            # else:
            #     errors.append(f'Expected "ID", but received {token}')


    def check_semicolon() -> None:
        matchs.append('SEMICOLON ok')
        match('SEMICOLON')
        if token_index >= token_count:
            print('\nFim do código')


    whilemark = ''
    while_go_to = ''
    def check_while() -> bool:
        nonlocal lmark, ifFALSE, last_token, whilemark, while_go_to
        last_token = token
        match('WHILE')
        matchs.append('WHILE ok')
        if token == 'LPAREN':
            match('LPAREN')
            matchs.append('LPAREN ok')
            if token == 'ID':
                relTEMP = check_id()
                if token == 'RPAREN':
                    match('RPAREN')
                    matchs.append('RPAREN ok')
                    if token == 'LBRACE':
                        match('LBRACE')
                        matchs.append('LBRACE ok')
                        ifFALSE = geraLabel()
                        geraCod('while '+relTEMP+' goto '+ifFALSE) # type: ignore
                        whilemark = ifFALSE
                        ifTRUE = geraLabel()
                        geraCod('goto '+ifTRUE+' :')
                        while_go_to = ifTRUE
                        
                        print(' ')
                        if token == 'ID':
                            check_id()
                            if token == 'IF':
                                check_if()
                                analyze_list(token)
                                if token == 'ELSE':
                                    check_else()
                                analyze_list(token)
                        if token == 'RBRACE':
                            geraCod(while_go_to+' :')
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


    lmark = ''
    ifFALSE = ''
    ifTRUE = ''
    ifmark = ''
    def check_if() -> None:
        nonlocal relTEMP, ifTRUE, ifFALSE, lmark, ifmark , last_token, last_go_to
        last_token = token
        match('IF')
        matchs.append('IF ok')
        if token == 'LPAREN':
            match('LPAREN')
            matchs.append('LPAREN ok')
            relTEMP = check_id()
            if token == 'RPAREN':
                match('RPAREN')
                matchs.append('RPAREN ok')
                if token == 'LBRACE':
                    matchs.append('LBRACE ok')
                    match('LBRACE')
                    if last_token =='':
                        ifFALSE = geraLabel()                 
                    geraCod('if '+relTEMP+' goto '+ifFALSE) # type: ignore
                    last_go_to = ifFALSE
                    lmark = ifTRUE
                    ifTRUE = geraLabel()
                    geraCod('goto '+ifTRUE+' :')
                    ifmark = ifTRUE
                    print(' ')
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


    last_token = ''
    def check_else() -> None:
        nonlocal last_token
        last_token = token
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
        opn = match('NUM')
        matchs.append('NUM ok')
        return opn


    def check_basic_arithmetic_expressions():
        if token in ['ADD', 'SUB', 'MUL', 'DIV']:
            lexOPA = match(token)
            matchs.append('Expressões aritméticas ok')
            return lexOPA
        elif token == 'POW':
            match('POW')
            if token == 'ID' or token == 'NUM':
                match(token)
                check_basic_arithmetic_expressions()

    def combined_assignment_operator():
        if token in ['ATRIB_ADD', 'ATRIB_SUB']:
            lexOPA = match(token)
            matchs.append('combined assignment operator ok')
            return lexOPA


    def check_arithmetic_expressions() -> None:
        if token == 'LPAREN':
            match('LPAREN')
            matchs.append('LPAREN ok')
            check_arithmetic_expressions()
            if token == 'RPAREN':
                match('RPAREN')
                matchs.append('RPAREN CLOSED ok')
                if token_index + 1 < token_count:
                    check_basic_arithmetic_expressions()
                    check_arithmetic_expressions()
            else:
                errors.append(f'Expected "RPAREN", but received {token}')
        elif token == 'NUM':
            matchs.append('NUM ok')
            lexema = match('NUM')
            check_basic_arithmetic_expressions()
            check_arithmetic_expressions()
        elif token == 'ID':
            check_id()
        elif token == 'LPAREN':
            matchs.append('LPAREN ok')


    def check_var() -> None:
        var = match('VAR')
        matchs.append('VAR ok')
        if token in ['INT', 'STR', 'REAL', 'BOOL']:
            type_var =  match(token)
            id_var = check_id()
            if not aft_comma:
                geraCod(var+ ' = '+type_var+' '+id_var) # type: ignore
            else:
                geraCod(var+ ' = '+type_var+' '+ aft_comma) # type: ignore
            print(' ')


    def show_list_checks() -> None:
        print('========== START ==========')
        for item in matchs:
            print(item)
        print('=========== END ===========')


    while token_index < token_count:
        if token == None:
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
        elif token not in ['VAR', 'ID', 'IF', 'WHILE']:
            if not matchs:
                errors.append(f"This token can not start a sentence: {token}")
            break
        else:
            errors.append(f"Invalid token: {token}")

    # if matchs:
    #     show_list_checks()

    return errors


def analyze_code(file_name: str) -> None:
    if analyze_code_with_verification(file_name):
        token_symbols, lexemas = get_tokens_code(file_name)
        errors = parser(token_symbols, lexemas)
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
