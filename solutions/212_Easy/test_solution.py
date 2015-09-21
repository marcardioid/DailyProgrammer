import unittest
from solution import *

class Test_212_Easy(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode("Jag talar Rövarspråket!"), "Jojagog totalolaror Rorövovarorsospoproråkoketot!")
        self.assertEqual(encode("I'm speaking Robber's language!"), "I'mom sospopeakokinongog Rorobobboberor'sos lolanongoguagoge!")
    def test_decode(self):
        self.assertEqual(decode("Jojagog totalolaror Rorövovarorsospoproråkoketot!"), "Jag talar Rövarspråket!")
        self.assertEqual(decode("I'mom sospopeakokinongog Rorobobboberor'sos lolanongoguagoge!"), "I'm speaking Robber's language!")

if __name__ == "__main__":
    unittest.main()