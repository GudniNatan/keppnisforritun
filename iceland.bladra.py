from sys import stdin

k, q = map(int, stdin.readline().split())
daemi = [0 for _ in range(k)]

for _ in range(q):
    a, b = map(int, stdin.readline().split())
    daemi[b - 1] += 1

print(min(daemi))
