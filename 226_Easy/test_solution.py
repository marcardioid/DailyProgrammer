import unittest
from solution import *

class Test_226_Easy(unittest.TestCase):
    def test_add_fractions(self):
        with open("input/input1.txt", "r") as file:
            lines = file.read().splitlines()
        fractions = [list(map(int, line.split('/'))) for line in lines[1:]]
        self.assertEqual(add_fractions(fractions), (7, 15))
        with open("input/input2.txt", "r") as file:
            lines = file.read().splitlines()
        fractions = [list(map(int, line.split('/'))) for line in lines[1:]]
        self.assertEqual(add_fractions(fractions), (2, 3))
        with open("input/input3.txt", "r") as file:
            lines = file.read().splitlines()
        fractions = [list(map(int, line.split('/'))) for line in lines[1:]]
        self.assertEqual(add_fractions(fractions), (89962, 58905))
        with open("input/input4.txt", "r") as file:
            lines = file.read().splitlines()
        fractions = [list(map(int, line.split('/'))) for line in lines[1:]]
        self.assertEqual(add_fractions(fractions), (351910816163, 29794134720))

if __name__ == "__main__":
    unittest.main()