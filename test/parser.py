from lexer import read_code, lexicon, verify_tokens


def analyze_code_with_verification(file_name, show_errors=True):
    if verify_tokens(file_name):
        print("Verificação de tokens bem-sucedida.")
        print("Começaremos o processo de analise sintática. Por favor, aguarde...")
        return True
    else:
        if show_errors:
            print("Erro: Token inválido encontrado.")
            print("Verifique o arquivo selecionado e tente novamente.")
        return False


analyze_code_with_verification('codigo.txt', show_errors=True)
