import random

class FalloutHackingGame:
    def __init__(self):
        self.guesses = 5
        self.difficulties = {1: (4, 5),
                             2: (6, 7),
                             3: (8, 9),
                             4: (10, 11, 12),
                             5: (13, 14, 15)}

    def input_difficulty(self):
        while True:
            d = input("Difficulty (1-5)? ")
            if d.isdigit() and 1 <= int(d) <= 5:
                return int(d)
            print("Please enter a number between 1 and 5 (inclusive).")

    def get_words(self, d):
        length = random.choice(self.difficulties[d])
        amount = random.choice(self.difficulties[d])
        with open("enable1.txt", "r") as file:
            words = random.sample([word for word in set(file.read().splitlines()) if len(word) == length], amount)
        return words

    def score(self, secret, guess):
        return sum([1 for (x, y) in zip(secret, guess) if x == y])

    def play(self):
        d = self.input_difficulty()
        clues = self.get_words(d)
        secret = random.choice(clues)
        # print("SOLUTION: {}".format(solution.upper()))
        print(*map(str.upper, clues), sep='\n')
        while self.guesses > 0:
            guess = input("Guess ({} left)? ".format(self.guesses))
            if len(guess) != len(secret):
                print("Please enter a word with {} characters!".format(len(secret)))
                continue
            s = self.score(secret, guess.lower())
            print("You guessed {}/{} characters correctly.".format(s, len(secret)))
            if len(secret) == s:
                print("You win! :>")
                return
            self.guesses -= 1
            if self.guesses == 0:
                print("Out of guesses... You lose! :< The solution was: '{}'!".format(secret.upper()))

if __name__ == "__main__":
    fhg = FalloutHackingGame()
    fhg.play()