def numtype(x):
    s = sum([i for i in range(1, x+1) if x % i == 0])
    if s == 2*x:
        return "perfect"
    else:
        return "deficient" if s < 2*x else "abundant by {}".format(s - 2*x)

if __name__ == "__main__":
    inputs = [18, 21, 6, 9, 111, 112, 220, 69, 134, 85, 28]
    for x in inputs:
        print("{}\t{}".format(x, numtype(x)))