import csv

n = int(input())
points = list()
for i in range(n):
    x, y = map(float, input().split())
    points.append((i, x, y))

with open("test.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    for p in points:
        writer.writerow(p)
