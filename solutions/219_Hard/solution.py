from itertools import combinations

def best_knapsack(filename):
    file = open(filename)
    capacity, total, *nuggets = map(float, file.read().split())
    file.close()
    best, result = total, []

    for i in range(0, int(total) + 1):
        for c in combinations(nuggets, i):
            node = capacity - sum(c)
            if 0 <= node < best:
                best = node
                result = c
    return result

if __name__ == "__main__":
    result = best_knapsack("input3.txt")
    print(sum(result))
    for nugget in result:
        print(nugget)
    print(result)