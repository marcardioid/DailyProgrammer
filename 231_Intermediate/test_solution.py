import unittest
from solution import *

class Test_231_Intermediate(unittest.TestCase):
    def test_find_sets(self):
        with open("input/input1.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(find_sets(lines), {('SP3F', 'DG3O', 'OR3H'), ('DG3O', 'SP3O', 'OR3O'), ('DG3O', 'SP1F', 'OR2H'), ('SP3F', 'SP3H', 'SP3O'), ('SP3F', 'SR1H', 'SG2O'), ('DR2F', 'SR1H', 'OR3O')})
        with open("input/input2.txt", "r") as file:
            lines = file.read().splitlines()
        self.assertEqual(find_sets(lines), {('DP1F', 'SR2F', 'OG3F'), ('DP1F', 'DG2H', 'DR3O'), ('SP1O', 'OG3F', 'DR2H'), ('OG3F', 'SP3H', 'DR3O'), ('DP2H', 'DG2H', 'DR2H'), ('SR2F', 'OR2O', 'DR2H')})

if __name__ == "__main__":
    unittest.main()