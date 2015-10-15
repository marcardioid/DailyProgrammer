import unittest
from solution import *

class Test_236_Intermediate(unittest.TestCase):
    def test_lowest_fibonacci_sequence(self):
        self.assertEqual(lowest_fibonacci_sequence(21)[1], 1)
        self.assertEqual(lowest_fibonacci_sequence(84)[1], 4)
        self.assertEqual(lowest_fibonacci_sequence(0)[1], 0)
        self.assertEqual(lowest_fibonacci_sequence(578)[1], 17)
        self.assertEqual(lowest_fibonacci_sequence(123456789)[1], 41152263)
        self.assertEqual(lowest_fibonacci_sequence(38695577906193299)[1], 7)

if __name__ == "__main__":
    unittest.main()