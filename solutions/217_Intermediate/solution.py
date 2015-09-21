from collections import OrderedDict

def encode(string, planet):
    lines = string.splitlines()

    dictionary = OrderedDict({
        "Omicron V": (lambda sentence: (str(ord(c) ^ 0b10000) for c in sentence)),
        "Hoth": (lambda sentence: (str(ord(c) + 10) for c in sentence)),
        "Ryza IV": (lambda sentence: (str(ord(c) - 1) for c in sentence)),
        "Htrae": (lambda sentence: (str(ord(c)) for c in reversed(sentence)))
    })

    output = []
    for line in lines:
        translation = dictionary[planet](line)
        output.append(' '.join(translation))
    return '\n'.join(output)

def decode(filename):
    with open(filename) as file:
        lines = file.read().splitlines()

    dictionary = OrderedDict({
        "Omicron V": (lambda word: (chr(int(c) ^ 0b10000) for c in word)),
        "Hoth": (lambda word: (chr(int(c) - 10) for c in word)),
        "Ryza IV": (lambda word: (chr(int(c) + 1) for c in word)),
        "Htrae": (lambda word: (chr(int(c)) for c in reversed(word)))
    })

    output = []
    for line in lines:
        words = line.split()
        translations = []
        for planet, decryption in dictionary.items():
            translations.append(''.join(decryption(words)))
        translation = max(translations, key=(lambda sentence: sum(c.isalpha() or c.isspace() for c in sentence) + int(1 if sentence[0].isupper() else 0)))
        planet = list(dictionary.keys())[translations.index(translation)]
        output.append(planet + " | " + translation)

    return '\n'.join(output)

if __name__ == "__main__":
    print(decode("input2.txt"))
    print(encode("We come in peace", "Omicron V"))