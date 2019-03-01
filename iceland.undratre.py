n, k = map(int, input().split())
i = h = 0
w = 1
if k != 1 and n > 1:
    while i < n:
        i += k ** h
        h += 1
    w = n - (n - 1) // k
else:
    h = n + 1

print(f"{h} {n + 1}\n1 {w}")
