from sys import stdin, stdout
from math import ceil, factorial
from functools import reduce
from operator import mul
from math import log, exp


def print(msg):
    stdout.write(str(msg))
    stdout.write("\n")


def prod(iterable):
    return reduce(mul, iterable, 1)


if __name__ == "__main__":
    input = stdin.readline
    total = 0
    days = 0
    n, p = map(int, input().split())
    bases = list(map(int, input().split()))
    for i, a in enumerate(bases):
        if a == 0:
            continue
        for j in range(i):
            total += a * bases[j]
            if total >= p:
                days += 1
                total -= p
    if total > 0:
        days += 1
    print(days)
