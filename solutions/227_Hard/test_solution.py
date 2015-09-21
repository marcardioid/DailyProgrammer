import unittest
from solution import *

class Test_227_Hard(unittest.TestCase):
    def test_build_matrix(self):
        with open("input/input1.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(build_matrix(lines), ["011", "101", "110"])
        with open("input/input2.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(build_matrix(lines), ["00010000", "00100000", "01001000", "10000001", "00100100", "00001001", "00000001", "00010110"])
        with open("input/input3.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(build_matrix(lines), ["0001", "0011", "0100", "1100"])
        with open("input/input4.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(build_matrix(lines), ["00110", "00001", "10010", "10101", "01010"])
        with open("input/input5.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(build_matrix(lines), ["0111", "1011", "1101", "1110"])

if __name__ == "__main__":
    unittest.main()