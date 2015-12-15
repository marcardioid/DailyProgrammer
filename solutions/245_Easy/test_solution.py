import unittest
from solution import *

class Test_245_Easy(unittest.TestCase):
    def test_date_to_iso_8601(self):
        self.assertEqual(date_to_iso_8601("2/13/15"), "2015-02-13")
        self.assertEqual(date_to_iso_8601("1-31-10"), "2010-01-31")
        self.assertEqual(date_to_iso_8601("5 10 2015"), "2015-05-10")
        self.assertEqual(date_to_iso_8601("2012 3 17"), "2012-03-17")
        self.assertEqual(date_to_iso_8601("2001-01-01"), "2001-01-01")
        self.assertEqual(date_to_iso_8601("2008/01/07"), "2008-01-07")

if __name__ == "__main__":
    unittest.main()