import unittest
from solution import *

class Test_242_Easy(unittest.TestCase):
    def test_weeks(self):
        self.assertEqual(weeks(15, 1), 5)
        self.assertEqual(weeks(200, 15), 5)
        self.assertEqual(weeks(50000, 1), 14)
        self.assertEqual(weeks(150000, 250), 9)

if __name__ == "__main__":
    unittest.main()