from random import randint
n = int(input())
band = list(map(int, input().split()))
# band = [randint(0, 1) for i in range(50)]
# band = list(map(int, "0 0 1 0 0 0 0 1 1 1 0 0 0 1 1 0 0 0 0 1 1 1 1 0 1 0 0 1 0 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 0 1 0 0 0 1".split()))
running = list()
potential = list()
total = 0
rev_total = 0
for b in band:
    total += b
    rev_total += int(not b)
    running.append(total)
    potential.append(rev_total)

combo = list()
for a, b in zip(running, potential):

    combo.append(b - a)

# print(*band)
# print(*running)
# print(*potential)
# print(*combo)
# print(sum(band))
# print(sum(combo))
start = combo.index(min(combo))
end = len(combo) - list(reversed(combo)).index(max(combo))
for i in range(start + 1, end):
    band[i] = int(not band[i])
print(sum(band))