"""
Introdução ao módulo Unittest

Unittest -> Testes unitários

O que são testes unitários? Teste unitário é a forma de se testar unidades de códigos fonte.

Unidade individuais podem ser: funções, métodos, classes, módulos etc.

# OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest. TestCase e a partir de então 
ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TesteCase -> Casos de teste para sua unidade.

# Conhecendo as assertions

Método                         Checa

assertEqual(a, b)              a == b
assertNotEqual(a, b)           a != b
assertTreu(x)                  x é verdadeiro
assertFalse(x)                 x é falso
assertIS(a, b)                 a é b
assertISNot(a, b)              a não é b
assertISNone(x)                x é None
assertIsNotNone(x)             x não é None
assertIn(a, b)                 a está em b
assertNotIn(a, b)              a não está em b
assertIsInstance(a, b)         a é instância de b
assertNotIsInstance(a, b)      a não é instância de b

Por convenção todos os testes em um test case devem ter seu nome iniciado com test_

# Para executar os testes com unittest

python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose

python nome_do_modulo -v

# Docstrings nos testes

Podemos acrescentar( e é recomendado) acrescentar docstrings nos nossos testes.
"""
# Prática - Utilizando a abordagem TDD

import unittest
from atividades import comer, dormir

class AtividadesTestes(unittest.TestCase):
    """Testando o retorno com comida saudável"""
    def test_comer_saudavel(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )
    
    def test_comer_gostosa(self):
        self.assertEqual(
            comer(comida='Pizza', saudavel=False),
            'Estou comendo Pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir 4h'
        )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Estou atrasado, pois dormi demais'
        )

if __name__ == '__main__':
    unittest.main()
