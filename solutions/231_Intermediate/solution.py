from itertools import combinations

def find_sets(cards):
    result = set()
    for triplet in combinations(cards, 3):
        if not any(len(set(card[i] for card in triplet)) == 2 for i in range(4)):
            result.add(triplet)
    return result

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        lines = file.read().splitlines()
    print(find_sets(lines))