n, x = map(int, input().split())

player = list()
for i in range(n):
    l, r, a = map(int, input().split())
    player.append((a, l, r))

player.sort()

print(high_score)