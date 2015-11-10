import random

def scramble(word):
    if len(word) <= 2:
        return word
    return word[0] + ''.join(random.sample(word[1:-1], len(word)-2)) + word[-1]

if __name__ == "__main__":
    sentence = "According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are,\n" \
               "the only important thing is that the first and last letter be in the right place.\n" \
               "The rest can be a total mess and you can still read it without a problem.\n" \
               "This is because the human mind does not read every letter by itself, but the word as a whole.\n" \
               "Such a condition is appropriately called Typoglycemia."
    print(' '.join(map(scramble, sentence.split())))