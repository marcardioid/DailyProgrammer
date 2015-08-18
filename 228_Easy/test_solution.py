import unittest
from solution import *

class Test_228_Easy(unittest.TestCase):
    def test_order(self):
        self.assertEqual(order("billowy"), "IN ORDER")
        self.assertEqual(order("defaced"), "NOT IN ORDER")
        self.assertEqual(order("sponged"), "REVERSE ORDER")

if __name__ == "__main__":
    unittest.main()