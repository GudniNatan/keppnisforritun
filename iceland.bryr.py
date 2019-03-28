from math import inf
from queue import PriorityQueue


class Graph:
    def __init__(self, n):
        self.vertices = set(i + 1 for i in range(n))
        self.edges = dict()

    def add_vertex(self, node):
        self.vertices.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = (to_node, length)
        if from_node in self.edges:
            from_node_edges = self.edges[from_node]
        else:
            self.edges[from_node] = dict()
            from_node_edges = self.edges[from_node]
        from_node_edges[to_node] = edge


def min_dist(q, dist):
    min_node = None
    for node in q:
        if min_node is None:
            min_node = node
        elif dist[node] < dist[min_node]:
            min_node = node

    return min_node


def dijkstra(graph, source, target):
    unvisited = set(graph.edges)
    dist = {node: inf for node in graph.nodes}
    dist[source] = 0

    while unvisited:
        u = min_dist(unvisited, dist)

        unvisited.remove(u)
        if u == target:
            return dist

        if u in graph.edges:
            for v in graph.edges[u].values():
                alt = dist[u] + v[1]
                if alt < dist[v[0]]:
                    dist[v[0]] = alt

    return dist


def dijkstra2(graph, source, target):
    dist = dict()
    dist[source] = 0
    q = PriorityQueue()
    for v in graph.vertices:
        if v != source:
            dist[v] = inf
        q.put(v, dist[v])

    while q:
        u = q.get()
        for v in graph.edges[u].values():
            alt = dist[u] + v[1]
            if alt < dist[v[0]]:
                dist[v[0]] = alt
    return dist


n, m = map(int, input().split())
g = Graph(n)
for i in range(m):
    a, b, c = map(int, input().split())
    g.add_edge(a, b, c)
    g.add_edge(b, a, c)

print(dijkstra2(g, 1, n)[n])
