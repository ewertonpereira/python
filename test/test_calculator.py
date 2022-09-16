import unittest
from calculator  import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()


    def test_sum_two_positive_numbers(self):
        result = self.calc.sum(2, 2)
        self.assertEqual(result, 4)


    def test_sum_two_negative_numbers(self):
        result = self.calc.sum(-2, -2)
        self.assertEqual(result, -4)


    def test_sum_two_stringss(self):
        with self.assertRaises(Exception):
            self.calc.sum('a', 'b')

if __name__ == '__main__':
    unittest.main()
