count = 0
for i in range(-50000, 50001):
    for j in range(max(-50000, -50000 - i), min(50001, 50001 - i)):
        count += 1
    if i % 1000 == 0:
        print(i)

print(count)
