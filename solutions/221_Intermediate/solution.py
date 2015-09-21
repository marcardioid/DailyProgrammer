def desnakify(filename):
    with open(filename) as file:
        lines = file.read().splitlines()[1:]

    matrix = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char.isalnum():
                matrix[(x, y)] = char

    words = []
    x, y = 0, 0
    shift = (1, 0) if (1, 0) in matrix else (0, 1)
    while True:
        word = ""
        word += matrix[(x, y)]

        dx, dy = shift
        while (x+dx, y+dy) in matrix:
            x, y = x+dx, y+dy
            word += matrix[(x, y)]
        words.append(word)

        shifts = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        shifts.remove((-shift[0], -shift[1]))
        for (ndx, ndy) in shifts:
            if (x+ndx, y+ndy) in matrix:
                shift = (ndx, ndy)
                break
        else:
            break
    return ' '.join(words)

if __name__ == "__main__":
    print(desnakify("input1.txt"))