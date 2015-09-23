import random

def print_house(blueprint):
    # Set up the walls / boundaries.
    walls = set()
    for y, l in enumerate(blueprint):
        for x, c in enumerate(l):
            if c == '*':
                for i in range(5):
                    for j in range(3):
                        walls.add((4 * x + i, 2 * y + j))

    # Translate the walls to ASCII.
    house = dict()
    for x, y in walls:
        neighbours = sum([1 for n in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)] if n in walls])
        if neighbours == 8:
            house[x, y] = ' '
        elif neighbours in (3, 7):
            house[x, y] = '+'
        else:
            house[x, y] = '-' if (x - 1, y) in walls and (x + 1, y) in walls else '|'

    # Randomly add windows.
    windows = [(x, y) for (x, y) in walls if (x % 4, y % 2) == (2, 1)]
    for (x, y) in windows:
        if random.random() < 0.5:
            house[x, y] = 'o'

    # Randomly add a door.
    floor = max(y for (x, y) in house) - 1
    x, y = random.choice([(x, y) for (x, y) in windows if y == floor])
    house[x - 1, y], house[x, y], house[x + 1, y] = '|', ' ', '|'

    # Add the rooftops.
    roofs = sorted([(x, y) for (x, y) in house if y != floor + 1 and house[x, y] == '+'])
    for i in range(0, len(roofs), 2):
        if roofs[i][1] != roofs[i + 1][1]:
            roofs[i + 1], roofs[i + 2] = roofs[i + 2], roofs[i + 1]
    for (x1, y1), (x2, y2) in zip(roofs[0::2], roofs[1::2]):
        for r in range(1, (x2 - x1) // 2):
            house[x1 + r, y1 - r], house[x2 - r, y1 - r] = '/', '\\'
        house[(x1 + x2) // 2, y1 - (x2 - x1) // 2] = 'A'

    # Print the house.
    xmin, xmax, ymin, ymax = min([x for (x, y) in house]), max([x for (x, y) in house]), min([y for (x, y) in house]), max([y for (x, y) in house])
    for y in range(ymin, ymax + 1):
        print(''.join([house.get((x, y), ' ') for x in range(xmin, xmax + 1)]))

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        num, *blueprint = file.read().splitlines()
    print_house(blueprint)