if __name__ == "__main__":
    with open("enable2.txt") as file:
        dictionary = set(file.read().splitlines())
    with open("challenge.txt") as file:
        haystack = file.read().splitlines()

    needles = []
    for i, line in enumerate(haystack):
        score = sum(word in dictionary for word in line.split())
        needles.append((i, line, score))
    needles.sort(key=(lambda s: (s[2], s[0])))

    poem = needles[-3:]
    for _, line, _ in poem:
        print(line)