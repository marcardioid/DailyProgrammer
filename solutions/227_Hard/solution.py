def build_matrix(lines):
    edges = {(0, 1): '-', (0, -1): '-', (1, 0): '|', (-1, 0): '|', (1, 1): '\\', (-1, -1): '\\', (1,-1): '/', (-1, 1): '/'}
    connections = {}
    rows = [list(l.rstrip()) for l in lines[1:]]

    def valid(y, x):
        return True if y >= 0 and y < len(rows) and x >= 0 and x < len(rows[y]) else False

    def trace(y, x, dy, dx, edge):
        while True:
            y, x = y + dy, x + dx
            c = rows[y][x] if valid(y, x) else ' '
            if c.isalpha():
                return c
            elif c == '#':
                rows[y][x] = ' '
                for (dy, dx), edge in edges.items():
                    if valid(y + dy, x + dx) and rows[y + dy][x + dx] == edge:
                        return trace(y, x, dy, dx, edge)
            elif c == edge:
                rows[y][x] = ' '

    for y, row in enumerate(rows):
        for x, a in enumerate(row):
            if a.isalpha():
                if not a in connections:
                    connections[a] = []
                for (dy, dx), edge in edges.items():
                    if valid(y + dy, x + dx) and rows[y + dy][x + dx] == edge:
                        b = trace(y, x, dy, dx, edge)
                        connections[a].append(b)
                        if not b in connections:
                            connections[b] = []
                        connections[b].append(a)

    matrix = []
    k = sorted(connections.keys())
    for y in k:
        matrix.append(''.join(['1' if x in connections[y] else '0' for x in k]))
    return matrix

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        lines = file.read().splitlines()
    print(build_matrix(lines))