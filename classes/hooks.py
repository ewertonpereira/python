"""
Unittest - Antes e após Hooks

Hooks -> São os testes em si. Ou seja, a execução dos testes.

setUp() -> É executado antes de cada método de teste. è útil para criarmos instâncias de objetos 
e outros dados.

tearDown() -> É executado ao final de cada teste. É útil para excluir dados ou fechar conexões com
bancos de dados.
"""
import unittest
from robo import Robo

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações ddo setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown vai rodar após o tesete
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown vai rodar após o tesete
        pass

    def tearDown(self):
        # Configurações ddo tearDown()
        pass

# Teste Robo

class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.robocop = Robo('Robocop', bateria=43)
        #print('setUp() sendo executado.')
    
    def test_carregar(self):
        self.robocop.carregar()
        self.assertEqual(self.robocop.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.robocop.dizer_nome(), 'BEEP BOOP BEEP BOOP. EU SOU ROBOCOP!')
        self.assertEqual(self.robocop.bateria, 42, 'A bateria deveria em 42%')

    def tearDown(self):
        #print('tearDeon() sendo executado.')
        pass


if __name__ == '__main__':
    unittest.main()
