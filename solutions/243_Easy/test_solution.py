import unittest
from solution import *

class Test_243_Easy(unittest.TestCase):
    def test_numtype(self):
        self.assertEqual(numtype(18), "abundant by 3")
        self.assertEqual(numtype(6), "perfect")
        self.assertEqual(numtype(9), "deficient")
        self.assertEqual(numtype(220), "abundant by 64")

if __name__ == "__main__":
    unittest.main()