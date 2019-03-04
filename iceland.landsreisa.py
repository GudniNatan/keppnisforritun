def read():
    points = list()
    with open("iceland.txt") as file:
        n = int(file.readline())
        for line in file:
            x, y = map(float, line.split())
            x *= 100000
            y *= 100000
            points.append((int(x), int(y)))
    return points


def get_dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def compute_dist_mat(points):
    dist_mat = list()
    for p1 in points:
        p1_dist = list()
        for p2 in points:
            p1_dist.append(get_dist(p1, p2))
        dist_mat.append(p1_dist)
    return dist_mat

points = read()

with open("test.txt", "w") as fptr:
        for i, p in enumerate(points):
                x, y = p
                fptr.write(f"{i} {x} {y}\n")

with open("tour.cyc") as fptr:
        print(*[line.strip() for line in fptr])
