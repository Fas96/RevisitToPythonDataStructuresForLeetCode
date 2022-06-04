import collections
from collections import deque


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

    def dijkstra(self, graph, initial):
        visited = {initial: 0}
        path = collections.defaultdict(list)

        nodes = set(graph.nodes)

        while nodes:
            minNode = None
            for node in nodes:
                if node in visited:
                    if minNode is None:
                        minNode = node
                    elif visited[node] < visited[minNode]:
                        minNode = node
            if minNode is None:
                break

            nodes.remove(minNode)
            currentWeight = visited[minNode]

            for edge in graph.edges[minNode]:
                weight = currentWeight + graph.distances[(minNode, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge].append(minNode)

        return visited, path


if __name__ == '__main__':
    g = Graph()
    g.addNode("0")
    g.addNode("1")
    g.addNode("2")
    g.addNode("3")
    g.addNode("4")
    g.addNode("5")
    g.addEdge("0", "1", 1)
    g.addEdge("1", "2", 4)
    g.addEdge("2", "3", 1)
    g.addEdge("3", "4", 4)
    g.addEdge("4", "5", 1)
    # g.bellmanFord("4")
    print(g.dijkstra(g, '1'))
    print(collections.defaultdict(list))
    d = collections.defaultdict(lambda: "Not Present")
    collections.deque()
    d["a"] = 1
    d["b"] = 2
