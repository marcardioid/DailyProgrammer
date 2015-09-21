from itertools import combinations

def segments(line):
    intersections = [i for i, c in enumerate(line) if c == '+']
    return combinations(intersections, 2)

def rectangles(lines):
    n = 0
    for i, line in enumerate(lines):
        for x, y in segments(line):
            for succeedingline in lines[i+1:]:
                if len(succeedingline) <= y or succeedingline[x] == ' ' or succeedingline[y] == ' ':
                    break
                if succeedingline[x] == '+' and succeedingline[y] == '+':
                    n += 1
    return n

if __name__ == "__main__":
    with open("input1.txt", "r") as file:
        lines = file.read().splitlines()
    print(rectangles(lines))
    with open("input2.txt", "r") as file:
        lines = file.read().splitlines()
    print(rectangles(lines))