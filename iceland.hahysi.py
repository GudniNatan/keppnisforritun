# n, m = map(int, input().split())
for n in range(2, 100):
    for m in range(2, 100):
        total = 0
        for i in range(n):
            for j in range(m):
                total += i * j

        print(m, n, total)
