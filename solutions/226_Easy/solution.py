def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def add_fractions(fractions):
    total = (0, 1)
    for fraction in fractions:
        total = (total[0] * fraction[1] + fraction[0] * total[1], total[1] * fraction[1])
        cd = gcd(total[0], total[1])
        total = (int(total[0] / cd), int(total[1] / cd))
    return total

if __name__ == "__main__":
    with open("input/input4.txt", "r") as file:
        lines = file.read().splitlines()
    fractions = [list(map(int, line.split('/'))) for line in lines[1:]]
    print("{}/{}".format(*add_fractions(fractions)))