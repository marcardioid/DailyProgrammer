import unittest
from solution import *

class Test_234_Intermediate(unittest.TestCase):
    def test_spellcheck(self):
        self.assertEqual(spellcheck("foobar"), "foob<ar")
        self.assertEqual(spellcheck("garbgae"), "garbg<ae")

if __name__ == "__main__":
    unittest.main()