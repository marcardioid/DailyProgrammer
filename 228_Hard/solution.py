import itertools

def golomb(order):
    def validate(edge):
        marks = set()
        for pair in itertools.combinations(edge, 2):
            mark = abs(pair[0] - pair[1])
            if mark in marks:
                return False
            marks.add(mark)
        return True

    for maximum in itertools.count(order):
        marks = range(0, maximum)
        for edge in [x for x in itertools.combinations(marks, order)]:
            if validate(edge):
                return edge

if __name__ == "__main__":
    for i in range(3, 8):
        ruler = golomb(i)
        print("{}\t{}\t->\t{}".format(i, max(ruler), ruler))