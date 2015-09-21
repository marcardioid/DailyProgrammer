def compatibility(x, y):
    return "{:032b}".format(x ^ y).count('0') / 32.0 * 100.0

def complement(x):
    return x ^ 0xFFFFFFFF

def match(x, y):
    print("The compatibility of {} and {} is {}%.".format(x, y, compatibility(x, y)))
    print("The number {} should avoid the number {}.".format(x, complement(x)))
    print("The number {} should avoid the number {}.".format(y, complement(y)))

if __name__ == "__main__":
    match(20, 65515)
    match(32000, 101)
    match(42000, 42)
    match(13, 12345)
    match(9999, 9999)
    match(8008, 37331)
    match(54311, 2)
    match(31200, 34335)