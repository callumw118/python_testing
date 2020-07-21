import unittest
from src.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2,3))
    
    def test_subtract(self):
        self.assertEqual(3, subtract(10,7))

    def test_multiply(self):
        self.assertEqual(10, multiply(5, 2))

    def test_divide(self):
        self.assertEqual(30, divide(300, 10))