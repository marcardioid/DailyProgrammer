import unittest
from solution import best_knapsack

class Test_219_Hard(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(best_knapsack("input1.txt"), (0.4109163, 0.6688261, 0.872064))
        self.assertEqual(best_knapsack("input2.txt"), (0.9185395, 0.2655587, 0.3373235, 0.8795087, 0.7802254, 0.8158674))

if __name__ == "__main__":
    unittest.main()