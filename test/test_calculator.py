import unittest
from calculator  import Calculator


class TestCalculatorSum(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()


    def test_sum_two_positive_numbers(self):
        result = self.calc.sum(2, 2)
        self.assertEqual(result, 4)


    def test_sum_two_negative_numbers(self):
        result = self.calc.sum(-2, -2)
        self.assertEqual(result, -4)


    def test_sum_two_strings(self):
        with self.assertRaises(Exception):
            self.calc.sum('a', 'b')


    def test_sum_two_float_numbers(self):
        result = self.calc.sum(2.0, 2.0)
        self.assertEqual(result, 4.0)


    def test_sum_number_string(self):
        with self.assertRaises(Exception):
            self.calc.sum(2, 'b')


    def test_sum_string_number(self):
        with self.assertRaises(Exception):
            self.calc.sum('a', 2)


if __name__ == '__main__':
    unittest.main()
