from sys import stdin, stdout


class LL(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        self.connections = 0

    def __eq__(self, value):
        return self.value

    def __str__(self):
        return "{}: {}, connections: {}".format(
            self.value, self.next, self.connections)


def node_dist(a, b, collections):
    for coll in collections:
        if a in coll:
            if b in coll:
                dist = coll[b] - coll[a]
                if dist >= 0:
                    return dist
    return -1


def seperate_nodes(nodes):
    collections = list()
    for node in nodes:
        if node.connections == 1:
            continue
        collections.append({node.value: 0})
        coll = collections[-1]
        hare = node.next
        while hare.value not in coll:
            coll[hare.value] = len(coll)
            hare = hare.next
    return collections


def print(str):
    stdout.write(str)
    stdout.write("\n")


if __name__ == "__main__":
    input = stdin.readline
    n = int(input())
    nodes = [LL(i + 1) for i in range(n)]
    for i in range(n):
        to = int(input())
        node_to = nodes[to - 1]
        nodes[i].next = node_to
        node_to.root = False
    collections = seperate_nodes(nodes)

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        print(str(node_dist(a, b, collections)))
    print(str(collections))
    print(str([str(node) for node in nodes]))
