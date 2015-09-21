from itertools import combinations

def closest_pair(points):
    points = [tuple(map(float, p.strip('()').split(','))) for p in points]
    min_dist, min_points = float('inf'), ()
    for ((x1, y1), (x2, y2)) in combinations(points, 2):
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) # No need to sqrt this as it doesn't change the ordering and is relatively slow.
        if dist < min_dist:
            min_dist, min_points = dist, ((x2, y2), (x1, y1))
    return min_points

if __name__ == "__main__":
    with open("input/input1.txt", "r") as file:
        num, *points = file.read().splitlines()
    print(closest_pair(points))