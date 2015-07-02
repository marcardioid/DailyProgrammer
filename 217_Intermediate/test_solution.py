import unittest
from solution import *

class Test_217_Intermediate(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(decode("input1.txt"), "Htrae: We come in Peace")

if __name__ == "__main__":
    unittest.main()