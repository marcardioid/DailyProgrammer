import unittest
from solution import *

class Test_222_Intermediate(unittest.TestCase):
    def test_desnakify(self):
        self.assertEqual(decrypt(encrypt("Attack at dawn", 1337), 1337), "Attack at dawn")


if __name__ == "__main__":
    unittest.main()