a, b, c = map(int, input().split())
if a ** 2 + b ** 2 == c ** 2:
    area = a * b / 2
    if int(area) == area:
        print(int(area))
    else:
        print(area)
else:
    print(-1)
