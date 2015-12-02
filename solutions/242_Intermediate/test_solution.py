import unittest
from solution import *

class Test_242_Intermediate(unittest.TestCase):
    def test_weeks(self):
        # with open("input/input1.txt", "r") as file:
        #     fav, *timetable = file.read().splitlines()
        # self.assertEqual(program(fav, timetable), ["Pokémon", "Law & Order", "The Fresh Prince of Bel-Air"])
        with open("input/input2.txt", "r") as file:
            fav, *timetable = file.read().splitlines()
        self.assertEqual(program(fav, timetable), ["The Fresh Prince of Bel-Air", "Ellen", "Quantum Leap"])

if __name__ == "__main__":
    unittest.main()