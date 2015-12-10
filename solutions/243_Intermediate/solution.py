from collections import defaultdict

def purchases(market, money):
    if money == 0:
        return [defaultdict(int)]
    elif money < 0 or not market:
        return []
    fruit, price = market[0]
    take = purchases(market, money - price)
    if take:
        take[0][fruit] += 1
    leave = purchases(market[1:], money)
    return take + leave

if __name__ == "__main__":
    with open("inputs/input1.txt", "r") as file:
        lines = file.read().splitlines()
    market = [(fruit, int(price)) for (fruit, price) in (line.split() for line in lines)]
    for basket in purchases(market, 500):
        print(", ".join(["{} {}".format(n, fruit + 's' if n > 1 else fruit) for fruit, n in basket.items()]))