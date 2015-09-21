import unittest
from solution import *

class Test_222_Easy(unittest.TestCase):
    def test_desnakify(self):
        self.assertEqual(balance("STEAD"), "S T EAD - 19")
        self.assertEqual(balance("CONSUBSTANTIATION"), "CONSUBST A NTIATION - 456")
        self.assertEqual(balance("WRONGHEADED"), "WRO N GHEADED - 120")
        self.assertEqual(balance("UNINTELLIGIBILITY"), "UNINTELL I GIBILITY - 521")
        self.assertEqual(balance("SUPERGLUE"), "SUPERGLUE DOES NOT BALANCE")

if __name__ == "__main__":
    unittest.main()