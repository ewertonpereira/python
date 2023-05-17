from typing import List
from lexer import read_code, lexicon, verify_tokens


def analyze_code_with_verification(file_name, show_errors=True):
    if verify_tokens(file_name):
        print("Verificação de tokens bem-sucedida.\nComeçaremos o processo de análise sintática. Por favor, aguarde...")
        return True
    else:
        error_message = "Erro: Token inválido encontrado.\nVerifique o arquivo selecionado e tente novamente."
        print(error_message) if show_errors else None
        return False



# analyze_code_with_verification('codigo.txt', show_errors=True)

def read_token_values(file_name: str) -> List[str]:
    with open(file_name, 'r') as file:
        code = file.read().split()
    
    return code




# print(token_values := read_token_values('codigo.txt'))
def process_code_file(file_name: str) -> None:
    if analyze_code_with_verification(file_name):
        token_symbols = read_token_values(file_name)
        print(token_symbols)
    else:
        print("Erro: O código não está de acordo com a gramática especificada.")



process_code_file('codigo.txt')


