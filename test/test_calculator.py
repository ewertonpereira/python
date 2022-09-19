import unittest
from unittest import result
from calculator  import Calculator


class TestCalculatorAddition(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()


    def test_addition_two_positive_numbers(self):
        result = self.calc.addition(2, 2)
        self.assertEqual(result, 4)


    def test_addition_two_negative_numbers(self):
        result = self.calc.addition(-2, -2)
        self.assertEqual(result, -4)


    def test_addition_two_strings(self):
        with self.assertRaises(Exception):
            self.calc.sum('a', 'b')


    def test_addition_two_float_numbers(self):
        result = self.calc.addition(2.0, 2.0)
        self.assertEqual(result, 4.0)


    def test_addition_number_string(self):
        with self.assertRaises(Exception):
            self.calc.addition(2, 'b')


    def test_addition_string_number(self):
        with self.assertRaises(Exception):
            self.calc.addition('a', 2)


class TestClaculatorSubtraction(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    
    def test_subtraction_two_positive_numbers(self):
        result = self.calc.subtraction(2, 1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
