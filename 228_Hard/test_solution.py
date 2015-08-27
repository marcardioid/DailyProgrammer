import unittest
from solution import *

class Test_228_Hard(unittest.TestCase):
    def test_golomb(self):
        self.assertEqual(golomb(3), (0, 1, 3))
        self.assertEqual(golomb(4), (0, 1, 4, 6))
        self.assertEqual(golomb(5), (0, 1, 4, 9, 11))

if __name__ == "__main__":
    unittest.main()