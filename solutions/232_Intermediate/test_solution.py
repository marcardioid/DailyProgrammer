import unittest
from solution import *

class Test_232_Intermediate(unittest.TestCase):
    def test_closest_pair(self):
        with open("input/input1.txt", "r") as file:
            num, *points = file.read().splitlines()
        self.assertEqual(closest_pair(points), ((6.625930036636377, 6.084986606308885), (6.422011725438139, 5.833206713226367)))
        with open("input/input2.txt", "r") as file:
            num, *points = file.read().splitlines()
        self.assertEqual(closest_pair(points), ((5.305665745194435, 5.6162850431000875), (5.333978668303457, 5.698128530439982)))

if __name__ == "__main__":
    unittest.main()