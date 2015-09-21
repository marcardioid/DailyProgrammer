import random

def snakify(sentence):
    words = sentence.split()
    offset = 0
    last = len(words) - 1
    for i, word in enumerate(words):
        if i % 2 == 0:
            if len(word) < offset and random.randrange(1, 100) < 50:
                offset -= len(word) - 1
                print(' ' * offset + word[::-1])
            else:
                print(' ' * offset + word)
                offset += len(word) - 1
        else:
            if i == last:
                for c in word[1:]:
                    print(' ' * offset + c)
            else:
                for c in word[1:-1]:
                    print(' ' * offset + c)

if __name__ == "__main__":
    snakify("SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE EPIC")