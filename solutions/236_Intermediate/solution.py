def fibonacci_multiplied(x):
    a, b = 0, x
    yield a
    while True:
        a, b = b, a + b
        yield a

def lowest_fibonacci_sequence(x):
    if x == 0:
        return [0, 0]
    multiplier = 1
    for n in fibonacci_multiplied(1):
        if n > x:
            break
        elif n > 0 and x % n == 0:
            if multiplier == 1 or x / n < multiplier:
                multiplier = x / n
    output = []
    for n in fibonacci_multiplied(int(multiplier)):
        if n > x:
            break
        output.append(n)
    return output

if __name__ == "__main__":
    integers = [21, 84, 0, 578, 123456789]
    for i in integers:
        print(lowest_fibonacci_sequence(i))