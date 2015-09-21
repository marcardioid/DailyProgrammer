import unittest
from solution import *

class Test_204_Intermediate(unittest.TestCase):
    def test_hypbin(self):
        self.assertEqual(hypbin(18), {1122, 1202, 1210, 2002, 2010, 10002, 10010})

if __name__ == "__main__":
    unittest.main()