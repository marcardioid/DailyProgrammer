def garland(word):
    return max([i if word[:i] == word[-i:] else 0 for i in range(len(word))])

def chain(word, repeat):
    degree = garland(word)
    return word + (word[degree:] * repeat) if degree > 0 else "Input word '{}' is not a garland word!".format(word)

if __name__ == "__main__":
    print(garland("programmer"))
    print(garland("ceramic"))
    print(garland("onion"))
    print(garland("alfalfa"))
    print(chain("ceramic", 3))