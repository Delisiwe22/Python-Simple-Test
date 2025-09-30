import unittest
from calculator import addition,subtraction ,multiplication, division, modulus
    


class TestCalculator(unittest.TestCase):

    def testAddition(self):
        self.assertEqual(addition(3, 2),5)

    def testSubtraction(self):
        self.assertEqual(subtraction(3,2),1)

    def testDivision(self):
        self.assertEqual(division(20, 10),2)

    def testMultiplication(self):
        self.assertEqual(multiplication(10,3),30)

    def testModulo(self):
        self.assertEqual(modulus(10,3),1)

if __name__== "__main__":
    unittest.main