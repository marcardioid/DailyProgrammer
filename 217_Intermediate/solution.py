from collections import OrderedDict

def decode(filename):
    with open(filename) as file:
        lines = file.read().splitlines()

    dictionary = OrderedDict({
        "Omicron V": (lambda sentence: (chr(int(c) ^ 0b10000) for c in sentence)),
        "Hoth": (lambda sentence: (chr(int(c) - 10) for c in sentence)),
        "Ryza IV": (lambda sentence: (chr(int(c) + 1) for c in sentence)),
        "Htrae": (lambda sentence: (chr(int(c)) for c in reversed(words)))
    })

    output = []
    for line in lines:
        words = line.split()
        translations = []
        for planet, decryption in dictionary.items():
            translations.append(''.join(decryption(words)))
        translation = max(translations, key=(lambda sentence: sum(c.isalpha() or c.isspace() for c in sentence)))
        planet = list(dictionary.keys())[translations.index(translation)]
        output.append(planet + " | " + translation)

    return '\n'.join(output)

if __name__ == "__main__":
    print(decode("input2.txt"))