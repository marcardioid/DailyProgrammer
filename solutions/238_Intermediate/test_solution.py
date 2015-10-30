import unittest
from solution import *

class Test_238_Intermediate(unittest.TestCase):
    def test_score(self):
        fhg = FalloutHackingGame()
        self.assertEqual(fhg.score("SCORPION", "SCORPION"), 8)
        self.assertEqual(fhg.score("SCORPION", "SCORPIOS"), 7)
        self.assertEqual(fhg.score("SCORPION", "FOOTNOTE"), 1)
        self.assertEqual(fhg.score("SCORPION", "REFINERY"), 0)

if __name__ == "__main__":
    unittest.main()