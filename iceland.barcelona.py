n, k = map(int, input().split())
toskur = list(map(int, input().split()))
if toskur[0] == k:
    print("fyrst")
elif toskur[1] == k:
    print("naestfyrst")
else:
    for i, t in enumerate(toskur):
        if t == k:
            print(i + 1, "fyrst")
