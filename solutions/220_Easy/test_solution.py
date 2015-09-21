import unittest
from solution import mangle

class Test_220_Easy(unittest.TestCase):
    def test_mangle(self):
        self.assertEqual(mangle("This challenge doesn't seem so hard."), "Hist aceeghlln denos't eems os adhr.")
        self.assertEqual(mangle("There are more things between heaven and earth, Horatio, than are dreamt of in your philosophy."), "Eehrt aer emor ghinst beeentw aeehnv adn aehrt, Ahioort, ahnt aer ademrt fo in oruy hhilooppsy.")
        self.assertEqual(mangle("Eye of Newt, and Toe of Frog, Wool of Bat, and Tongue of Dog."), "Eey fo Entw, adn Eot fo Fgor, Loow fo Abt, adn Egnotu fo Dgo.")
        self.assertEqual(mangle("Adder's fork, and Blind-worm's sting, Lizard's leg, and Howlet's wing."), "Adder's fkor, adn Bdilm-nors'w ginst, Adilrs'z egl, adn Ehlost'w ginw.")
        self.assertEqual(mangle("For a charm of powerful trouble, like a hell-broth boil and bubble."), "For a achmr fo eflopruw belortu, eikl a behh-llort bilo adn bbbelu.")

if __name__ == "__main__":
    unittest.main()