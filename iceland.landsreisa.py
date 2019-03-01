from random import shuffle

n = int(input())
points = list()
for i in range(n):
    x, y = map(float, input().split())
    points.append((x, y, i))


def get_dist(points):
    dist = 0
    last_x, last_y, i = points[-1]
    for x, y, i in points:
        dist += ((x - last_x) ** 2 + (y - last_y) ** 2) ** 0.5
        last_x, last_y = x, y
    return dist



best_dist = get_dist(points)
best_points = points.copy()

for i in range(10000):
    shuffle(points)
    dist = get_dist(points)
    if dist < best_dist:
        best_dist = dist
        best_points = points.copy()

print(dist)
print(" ".join([str(points[i][2]) for i in range(n)]))
