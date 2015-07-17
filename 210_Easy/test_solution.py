import unittest
from solution import *

class Test_210_Easy(unittest.TestCase):
    def test_compatibility(self):
        self.assertEqual(compatibility(20, 65515), 50.0)
        self.assertEqual(compatibility(54311, 2), 78.125)
    def test_complement(self):
        self.assertEqual(complement(20), 4294967275)
        self.assertEqual(complement(2), 4294967293)

if __name__ == "__main__":
    unittest.main()