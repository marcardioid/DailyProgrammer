import unittest
from solution import *

class Test_223_Easy(unittest.TestCase):
    def test_desnakify(self):
        self.assertEqual(garland("programmer"), 0)
        self.assertEqual(garland("ceramic"), 1)
        self.assertEqual(garland("onion"), 2)
        self.assertEqual(garland("alfalfa"), 4)
        self.assertEqual(chain("ceramic", 3), "ceramiceramiceramiceramic")

if __name__ == "__main__":
    unittest.main()