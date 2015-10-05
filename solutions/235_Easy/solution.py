def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_ruth_aaron(pair):
    return sum(set(prime_factors(pair[0]))) == sum(set(prime_factors(pair[1])))

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        num, *pairs = file.read().splitlines()
    for pair in pairs:
        print("{} {}".format(pair, "VALID" if is_ruth_aaron(eval(pair)) else "NOT VALID"))
