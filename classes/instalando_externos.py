"""
Módulos Externos

Utilizamos o gerenciador de pacotes Pythpn chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: 

https://pypi.org

Colorama -> É utilizado para permitir impressão de textos coloridos no terminal

Instalando um módulo

pip install nome do módulo
"""
from colorama import init, Fore, Back, Style

init()

print(Fore.RED + 'Ewerton Pereira')
print(Back.BLUE + 'Ewerton Pereira')
print(Style.DIM + 'Ewerton Pereira')
print(Style.RESET_ALL)
print('back to normal now')
