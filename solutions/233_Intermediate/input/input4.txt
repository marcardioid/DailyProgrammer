import random

def next_generation(generation):
    w, h = max([len(line) for line in generation]), len(generation)
    generation = [line.ljust(w) for line in generation]

    def next_state(x, y):
        neighbours = ''.join([generation[y][x] if 0 <= x < w and 0 <= y < h else ' ' for (x, y) in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)]])
        neighbours = neighbours.replace(' ', '')
        cell, score = generation[y][x].strip(), len(neighbours)
        if cell and score in (2, 3):
            return cell
        elif not cell and score == 3:
            return random.choice([neighbour for neighbour in neighbours])
        else:
            return ' '

    return [''.join([next_state(x, y) for x in range(w)]) for y in range(h)]

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        generation = file.read().splitlines()
    for line in next_generation(generation):
        print(line)