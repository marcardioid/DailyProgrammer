import unittest
from solution import *

class Test_232_Easy(unittest.TestCase):
    def test_is_palindrome(self):
        with open("input/input1.txt", "r") as file:
            num, *lines = file.read().splitlines()
        self.assertEqual(is_palindrome(lines), "Palindrome")
        with open("input/input2.txt", "r") as file:
            num, *lines = file.read().splitlines()
        self.assertEqual(is_palindrome(lines), "Not a palindrome")
        with open("input/input3.txt", "r") as file:
            num, *lines = file.read().splitlines()
        self.assertEqual(is_palindrome(lines), "Not a palindrome")
        with open("input/input4.txt", "r") as file:
            num, *lines = file.read().splitlines()
        self.assertEqual(is_palindrome(lines), "Palindrome")

if __name__ == "__main__":
    unittest.main()