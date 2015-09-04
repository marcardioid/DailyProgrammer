from itertools import chain, zip_longest

with open("dictionary.txt", "r") as file:
    dictionary = set(file.read().splitlines())

def match(word):
    if len(word) < 2:
        return False
    elif word.lower() in dictionary:
        return word
    elif word.lower()[::-1] in dictionary:
        return word[::-1]
    else:
        return max(match(word[1:]), match(word[:-1]), key=len)

def decompact(logo):
    words = []
    possibilities = list(chain.from_iterable(map(str.split, logo))) + list(chain.from_iterable(map(str.split, map(''.join, zip_longest(*logo, fillvalue='')))))
    for word in [word for word in map(match, possibilities) if word]:
        words.append(word.lower())
    return sorted(words)

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        lines = file.read().splitlines()
    for word in decompact(lines[1:]):
        print(word)