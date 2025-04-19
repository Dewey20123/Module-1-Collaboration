import unittest
from __init__ import sum  # ← works because __init__.py is in same folder
from fractions import Fraction

class TestSum(unittest.TestCase):

    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)  # This one will fail on purpose

if __name__ == '__main__':
    unittest.main()