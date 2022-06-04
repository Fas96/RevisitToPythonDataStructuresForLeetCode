import collections


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Distance of Vertex from Source")
        for key, value in dist.items():
            print('  ' + key, ' :    ', value)

    # Implementing Bellman-Ford's Algorithm
    def bellmanFord(self, src):
        dist = {i: float("Inf") for i in self.nodes}
        dist[src] = 0

        for temp in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative cycle")
                return

        self.print_solution(dist)

    # Implementing Dijkstra's Algorithm
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

            for edge in graph[minNode]:
                weight = currentWeight + graph.distances[(minNode, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge].append(minNode)

        return visited, path


if __name__ == '__main__':
    g = Graph(6)
    g.addNode("0")
    g.addNode("1")
    g.addNode("2")
    g.addNode("3")
    g.addNode("4")
    g.addNode("5")
    g.add_edge("0", "1", 1)
    g.add_edge("1", "2", 4)
    g.add_edge("2", "3", 1)
    g.add_edge("3", "4", 4)
    g.add_edge("4", "5", 1)
    g.bellmanFord("0")
    # g.dijkstra(g, '0')