import unittest


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


    def test_subtraction_two_negative_numbers(self):
        result = self.calc.subtraction(-3, -6)
        self.assertEqual(result, 3)


    def test_subtraction_float_numbers(self):
        result = self.calc.subtraction(4.2, 2.5)
        self.assertEqual(round(result, 2), 1.70)


    def test_subtraction_two_strings(self):
        with self.assertRaises(Exception):
            self.calc.subtraction('a','b')


    def test_subtraction_string_number(self):
        with self.assertRaises(Exception):
            self.calc.subtraction('a', 3)


    def test_subtraction_number_string(self):
        with self.assertRaises(Exception):
            self.calc.subtraction(8, 'b')


class TesteCalculatorMultiplication(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()


    def test_multiplication_two_positive_numbers(self):
        result = self.calc.multiplication(2, 2)
        self.assertEqual(result, 4)

    
    def test_multiplication_two_negative_numbers(self):
        result = self.calc.multiplication(-7, -2)
        self.assertEqual(result, 14)


    def test_multiplication_two_float_numbers(self):
        result = self.calc.multiplication(7.1, 2.6)
        self.assertEqual(result, 18.46)


    def test_multiplication_strings(self):
        with self.assertRaises(Exception):
            self.calc.multiplication('a', 'b')

    def test_mulplication_string_number(self):
        with self.assertRaises(Exception):
            self.calc.multiplication('a', 2)


    def test_multiplication_number_string(self):
        with self.assertRaises(Exception):
            self.calc.multiplication(2, 'b')


class TestCalculatorDivision(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()


    def test_division_by_zero(self):
        with self.assertRaises(Exception):
            self.calc.division(2, 0)


    def test_division_two_positive_numbers(self):
        result = self.calc.division(4, 2)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
