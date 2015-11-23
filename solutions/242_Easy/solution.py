def weeks(people, fruits):
    harvest, weeks = 0, 1
    while harvest < people:
        weeks += 1
        harvest += fruits
        fruits += harvest
    return weeks

if __name__ == "__main__":
    inputs = [(15, 1), (200, 15), (50000, 1), (150000, 250)]
    for x, y in inputs:
        print(weeks(x, y))