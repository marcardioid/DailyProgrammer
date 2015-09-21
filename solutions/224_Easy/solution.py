from random import randrange

def shuffle(list):
    """Shuffles (Knuth) a finite list in place."""
    for i in range(len(list) - 1, 0, -1):
        j = randrange(i + 1)
        list[i], list[j] = list[j], list[i]

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    for line in lines:
        list = line.split()
        shuffle(list) # Not that different from random.shuffle(list), but I wanted to write it myself.
        print(list)