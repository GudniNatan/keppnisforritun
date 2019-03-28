from sys import stdin, stdout
from math import inf


def print(str):
    stdout.write(str)
    stdout.write("\n")


def shortestPaths(mat, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                mat[j][k] = min(mat[j][k], mat[j][i] + mat[i][k])
    return mat


input = stdin.readline
n, m, q = map(int, input().split())
while n != 0:
    mat = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        mat[i][i] = 0
    for i in range(m):
        u, v, w = map(int, input().split())
        mat[u][v] = min(mat[u][v], w)
    shortest = shortestPaths(mat, n)
    for i in range(q):
        u, v = map(int, input().split())
        if shortest[u][v] == inf:
            print("Impossible")
        elif shortest[u][v] < 0:
            print("-Infinity")
        else:
            print(str(shortest[u][v]))
    stdout.write("\n")
    n, m, q = map(int, input().split())
