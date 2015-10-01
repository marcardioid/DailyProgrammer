from itertools import combinations_with_replacement
from functools import reduce

def find_vampires(num_digits, num_fangs):
    vampires = dict()
    for fangs in combinations_with_replacement(range(10 ** (num_digits // num_fangs - 1), 10 ** (num_digits // num_fangs)), num_fangs):
        vampire = reduce(lambda x, y: x * y, fangs)
        if vampire in vampires.keys() or sorted(''.join(map(str, fangs))) != sorted(str(vampire)):
            continue
        vampires[vampire] = fangs
    return sorted(vampires.items())

if __name__ == "__main__":
    for vampire, fangs in find_vampires(4, 2):
        print("{}={}".format(vampire, '*'.join(map(str, fangs))))