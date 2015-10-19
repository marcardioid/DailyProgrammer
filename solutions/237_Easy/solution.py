with open("enable1.txt", "r") as file:
    dictionary = set(file.read().splitlines())

def brokenkeyboard(ls):
    return max([w for w in dictionary if set(w).issubset(ls)], key=lambda x: len(x))

if __name__ == "__main__":
    with open("input/input2.txt", "r") as file:
        lines = file.read().splitlines()
    for ls in lines:
        print("{}\t:\t{}".format(ls, brokenkeyboard(ls)))