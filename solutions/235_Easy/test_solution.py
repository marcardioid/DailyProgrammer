import unittest
from solution import *

class Test_235_Easy(unittest.TestCase):
    def test_is_ruth_aaron(self):
        self.assertEqual(is_ruth_aaron((714, 715)), True)
        self.assertEqual(is_ruth_aaron((77, 78)), True)
        self.assertEqual(is_ruth_aaron((20, 21)), False)
        self.assertEqual(is_ruth_aaron((5, 6)), True)
        self.assertEqual(is_ruth_aaron((2107, 2108)), True)
        self.assertEqual(is_ruth_aaron((492, 493)), True)
        self.assertEqual(is_ruth_aaron((128, 129)), False)

if __name__ == "__main__":
    unittest.main()