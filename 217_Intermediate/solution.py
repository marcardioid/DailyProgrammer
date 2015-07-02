def decode(filename):
    with open(filename) as file:
        lines = file.read().splitlines()

    planets = ["Omicron V", "Hoth", "Ryza IV", "Htrae"]
    score = lambda sentence: sum(c.isalpha() or c.isspace() for c in sentence)
    output = []
    for line in lines:
        words = line.split()
        translations = [
            "".join(chr(int(c) ^ 0b10000) for c in words),
            "".join(chr(int(c) - 10) for c in words),
            "".join(chr(int(c) + 1) for c in words),
            "".join(chr(int(c)) for c in reversed(words))
        ]
        translation = max(translations, key=score)
        planet = planets[translations.index(translation)]
        output.append(planet + " | " + translation)

    return ' '.join(output)

if __name__ == "__main__":
    print(decode("input.txt"))