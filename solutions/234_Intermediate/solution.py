with open("enable1.txt") as file:
    dictionary = set(file.read().splitlines())

def spellcheck(word):
    fault = None
    for n in range(len(word) + 1):
        if not any(x.startswith(word[:n]) for x in dictionary):
            fault = "{}<{}".format(word[:n], word[n:])
            break
    return fault if fault else "CORRECT"

if __name__ == "__main__":
    with open("input/input2.txt", "r") as file:
        words = file.read().splitlines()
    for word in words:
        print("{}\t{}".format(word, spellcheck(word)))