import unittest
from calculator import addition, subtraction, multiplication, division, modulus, exponentiation, floor_division, calculator

class TestCalculator(unittest.TestCase):
    def testAddition(self):
        self.assertEqual(addition(3, 2), 5)

    def testSubtraction(self):
        self.assertEqual(subtraction(3, 2), 1)

    def testDivision(self):
        self.assertEqual(division(20, 10), 2)

    def testMultiplication(self):
        self.assertEqual(multiplication(10, 3), 30)

    def testModulo(self):
        self.assertEqual(modulus(10, 3), 1)

    def testExponentiation(self):
        self.assertEqual(exponentiation(2, 3), 8)

    def testFloor_Division(self):
        self.assertEqual(floor_division(9, 4), 2)

    def test_calculator_addition(self):
        self.assertEqual(calculator(2, '+', 3), 5)
        self.assertEqual(calculator(-1, '+', 1), 0)

    def test_calculator_subtraction(self):
        self.assertEqual(calculator(5, '-', 2), 3)
        self.assertEqual(calculator(0, '-', 5), -5)

    def test_calculator_multiplication(self):
        self.assertEqual(calculator(4, '*', 3), 12)
        self.assertEqual(calculator(-2, '*', 3), -6)

    def test_calculator_division(self):
        self.assertEqual(calculator(10, '/', 2), 5)
        self.assertAlmostEqual(calculator(7, '/', 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            calculator(5, '/', 0)

    def test_calculator_modulus(self):
        self.assertEqual(calculator(10, '%', 3), 1)
        self.assertEqual(calculator(9, '%', 3), 0)

    def test_calculator_exponentiation(self):
        self.assertEqual(calculator(2, '**', 3), 8)
        self.assertEqual(calculator(5, '**', 0), 1)

    def test_calculator_floor_division(self):
        self.assertEqual(calculator(7, '//', 2), 3)
        self.assertEqual(calculator(9, '//', 3), 3)
        with self.assertRaises(ZeroDivisionError):
            calculator(5, '//', 0)



if __name__ == "__main__":
    unittest.main()