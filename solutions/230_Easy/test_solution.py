import unittest
from solution import *

class Test_230_Easy(unittest.TestCase):
    def test_find(self):
        self.assertEqual(" -> ".join(map(str, find(json.load(open("input/input1.txt", "r")), "dailyprogrammer", [])[::-1])), "favoriteWebsites -> 1")
        self.assertEqual(" -> ".join(map(str, find(json.load(open("input/input2.txt", "r")), "dailyprogrammer", [])[::-1])), "caki -> cyd -> qembsejm -> 1")
        self.assertEqual(" -> ".join(map(str, find(json.load(open("input/input3.txt", "r")), "dailyprogrammer", [])[::-1])), "axvjf -> tskgrsi -> 0 -> ozr -> 0 -> 1 -> 0")
        self.assertEqual(" -> ".join(map(str, find(json.load(open("input/input4.txt", "r")), "dailyprogrammer", [])[::-1])), "myutkqsfzw -> 4 -> fxeu -> 1 -> 0 -> 1 -> 2 -> 7 -> ocjcjokh -> xqfbrz -> 0")

if __name__ == "__main__":
    unittest.main()