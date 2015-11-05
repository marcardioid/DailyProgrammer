def game_of_threes(x):
    while x != 1:
        if x % 3 == 0:
            print(int(x), 0)
        elif (x - 1) % 3 == 0:
            print(int(x), -1)
            x -= 1
        else:
            print(int(x), 1)
            x += 1
        x /= 3
    print(1)

if __name__ == "__main__":
    inputs = [100, 31337357]
    for i in inputs:
        game_of_threes(i)