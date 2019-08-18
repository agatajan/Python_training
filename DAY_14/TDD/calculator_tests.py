from unittest import TestCase
from DAY_14.TDD.tests_script import Calculator


class CalculatorTests(TestCase):

    def test_multiply_values(self):
        multiply_result = Calculator.multiply(2, 3)
        self.assertEqual(6, multiply_result, "Multiplying 2 by 3 should be 6")

    def test_exponentiation(self):
        exponentiation_result = Calculator.exponentiation(2, 2)
        self.assertEqual(4, exponentiation_result, "Exponentiation result should be 4")


