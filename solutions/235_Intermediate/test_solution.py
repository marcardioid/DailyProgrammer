import unittest
from solution import *

class Test_235_Intermediate(unittest.TestCase):
    def test_calculate_score(self):
        self.assertEqual(calculate_score(['X', 'X', 'X' 'X', 'X', 'X', 'X', 'X', 'X', 'XXX']), 300)
        self.assertEqual(calculate_score(['X', '-/', 'X' '5-', '8/', '9-', 'X', '81', '1-', '4/X']), 137)
        self.assertEqual(calculate_score(['62', '71', 'X' '9-', '8/', 'X', 'X', '35', '72', '5/8']), 140)

if __name__ == "__main__":
    unittest.main()