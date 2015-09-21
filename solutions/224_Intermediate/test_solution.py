import unittest
from solution import *

class Test_224_Intermediate(unittest.TestCase):
    def test_rectangles(self):
        with open("input1.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(rectangles(lines), 25)
        with open("input2.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(rectangles(lines), 25)

if __name__ == "__main__":
    unittest.main()