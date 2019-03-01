from sys import stdin, stdout


def starwars(numbers, n):
    numbers.sort()
    for i in range(n, n + n):
        yield numbers[i]
    for i in range(n):
        yield numbers[i]
    for i in range(n * 2, n * 3):
        yield numbers[i]


if __name__ == "__main__":
    input = stdin.readline
    n = int(input()) // 3
    nums = list(map(int, input().split()))
    order = starwars(nums, n)
    print(*order)
