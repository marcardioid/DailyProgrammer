import unittest
from solution import *

class Test_237_Easy(unittest.TestCase):
    def test_calculate_score(self):
        self.assertEqual(brokenkeyboard("abcd"), "bacca")
        self.assertEqual(brokenkeyboard("qwer"), "weewee")
        self.assertEqual(brokenkeyboard("hjklo"), "holloo")

if __name__ == "__main__":
    unittest.main()