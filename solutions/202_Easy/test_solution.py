import unittest
from solution import *

class Test_202_Easy(unittest.TestCase):
    def test_binarytoascii(self):
        self.assertEqual(binarytoascii(b"0100100001100101011011000110110001101111001000000101011101101111011100100110110001100100"), "Hello World")

if __name__ == "__main__":
    unittest.main()