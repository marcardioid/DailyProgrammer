import unittest
from solution import *

class Test_227_Intermediate(unittest.TestCase):
    def test_find_chains(self):
        with open("input/input1.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(len(find_chains(lines)), 1)
        with open("input/input2.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(len(find_chains(lines)), 3)
        with open("input/input3.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(len(find_chains(lines)), 1)
        with open("input/input4.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(len(find_chains(lines)), 9)

if __name__ == "__main__":
    unittest.main()