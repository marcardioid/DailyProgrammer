import unittest
from solution import *

class Test_231_Hard(unittest.TestCase):
    def test_find_stable_marriages(self):
        preferences = {}
        with open("input/input1.txt", "r") as file:
            for line in file.read().splitlines():
                person, *options = line.split(', ')
                preferences[person] = options
        self.assertEqual(find_stable_marriages(preferences), {'a': 'B', 'b': 'A', 'c': 'C'})

if __name__ == "__main__":
    unittest.main()