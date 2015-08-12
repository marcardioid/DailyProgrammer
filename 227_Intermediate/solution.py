def find_chains(lines):
    matrix = []
    for y, line in enumerate(lines[1:]):
        for x, char in enumerate(line):
            if char == 'x':
                matrix.append((x, y))
    chains = []
    for pos in matrix:
        if not any([pos in chain for chain in chains]):
            chains.append(build_chain(pos, matrix))
    return chains

def build_chain(start, matrix):
    chain = [start]
    forks = [start]
    while forks:
        mutablecopy = forks.copy()
        for (x, y) in mutablecopy:
            for neighbour in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                if neighbour not in chain and neighbour in matrix:
                    chain.append(neighbour)
                    forks.append(neighbour)
            forks.remove((x, y))
    return chain

if __name__ == "__main__":
    with open("input/input4.txt", "r") as file:
        lines = file.read().splitlines()
    print(len(find_chains(lines)))