"""
Unittest - Outros tipos de assertion

"""
import unittest
from atividades import engracada

class AtividadesTestes:

    def test_engracada(self):
        #self.assertEqual(engracada('Sérgio Malandro'),False)
        self.assertFalse(engracada('Sérgio Malandro'))
        self.assertTrue(engracada('Murilo Couto')), 'Murilo Couto deveria ser engraçado'


if __name__ == '__main__':
    unittest.main()
