from random import randint


class Node(object):
    def __init__(self, *args, **kwargs):
        self.connection = None
        self.net = {self, }

    def connect(self, other):
        self.connection = other
        net = other.net
        net.update(self.net)
        for node in self.net:
            node.net = net

n = 5
count = 0
iterations = 1000000

for i in range(iterations):
    nodes = [Node() for _ in range(n)]
    for j in range(n):
        node = nodes[j]
        num = randint(0, n-2)
        if num >= j:
            num += 1
        node.connect(nodes[num])
    if len(nodes[0].net) == n:
        count += 1

print(count)
print(count / iterations)
print("approx", (n-1)**n - ((n-1) ** n * count / iterations))