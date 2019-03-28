def find_candidate_keys(A, F):
    n = 1
    i = 0
    K = [A]
    keys = list()
    while i < n:
        for a, b in F:
            a_set = set((a,))
            S = a_set.union(K[i].difference(set((b,))))
        found = False
        for j in range(n - 1):
            if K[j] >= S:
                found = True
                keys.append(a)
        if not found:
            K.append(S)
            n += 1
        i += 1
    return keys


attributes = set(("A", "B", "C", "D"))
fd1 = ("B", "C")
fd2 = ("D", "A")
F = [fd2, fd1,]
print(find_candidate_keys(attributes, F))
