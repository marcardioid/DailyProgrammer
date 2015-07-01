import unittest
from solution import *

class Test_221_Intermediate(unittest.TestCase):
    def test_desnakify(self):
        self.assertEqual(desnakify("input1.txt"), "SNAKE EATS SALSA AND DUSTY YUMMY YACHTS")
        self.assertEqual(desnakify("input2.txt"), "WIZARDRY YAWN NORDIC CAR RED DINOSAUR REACT TO OVAL LEGS SUBTLY")
        self.assertEqual(desnakify("input3.txt"), "NUMEROUS SYMBOLIC CUSTARDS SYMBOL LUXURY YEAR ROAD DO")
        self.assertEqual(desnakify("input4.txt"), "RESIGN NULL LAG GRAPES SHOT TIGER RETURN NOTHING GRAND DELIGHTFUL LANTERNS SO")

if __name__ == "__main__":
    unittest.main()