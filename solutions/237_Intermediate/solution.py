def fill(grid):
    legend = {0: '#',
              1: '=',
              2: '-',
              3: '.'}
    grid = {(x, y): grid[y][x] for y in range(h) for x in range(w)}
    def flood(root=(1, 1), depth=0):
        visited = set()
        queue = {root}
        while queue:
            node = queue.pop()
            if node in visited:
                continue
            visited.add(node)
            if grid[node] == '+' and grid[(node[0]+1, node[1])] == '-' and grid[(node[0], node[1]+1)] == '|':
                flood((node[0]+1, node[1]+1), depth+1)
            elif grid[node] == ' ':
                grid[node] = legend.get(depth, ' ')
                for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    if (node[0]+dx, node[1]+dy) in grid:
                        queue.add((node[0]+dx, node[1]+dy))
    flood()
    return grid

if __name__ == "__main__":
    with open("input/input.txt", "r") as file:
        dimensions, *data = file.read().splitlines()
    h, w = map(int, dimensions.split())
    grid = fill(data)
    print('\n'.join(''.join(grid[(x, y)] for x in range(w)) for y in range(h)))