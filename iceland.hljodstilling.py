from itertools import combinations


def main():
    L, R, k = map(int, input().split())
    nums = set(map(int, input().split()))
    L -= 1

    if 1 in nums:
        print(R - L)
        return

    total = 0
    combined = list()
    for i in range(2, k + 1):
        for c in combinations(nums, i):
            product = 1
            for item in c:
                product *= item
            if product <= R:
                combined.append(product)

    for n in nums:
        total += R // n
    for n in combined:
        total -= R // n
    for n in nums:
        total -= L // n
    for n in combined:
        total += L // n

    print(total)

main()