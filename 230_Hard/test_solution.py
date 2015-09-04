import unittest
from solution import *

class Test_230_Hard(unittest.TestCase):
    def test_decompact(self):
        with open("input/input1.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(decompact(lines[1:]), ["aniseed", "british", "dishes", "nastily", "road", "yoke"])
        with open("input/input2.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(decompact(lines[1:]), ["dividend", "fluctuate", "fourteen", "nickel"])
        with open("input/input3.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(decompact(lines[1:]), ["cardboard", "coating", "declension", "garden", "graphic", "shepherd", "yellow"])

if __name__ == "__main__":
    unittest.main()