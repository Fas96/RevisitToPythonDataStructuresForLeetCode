class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_Edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for others in self.adj_list[vertex]:
                self.adj_list[others].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def print_Graph(self):
        for v in self.adj_list:
            print(v, ':', self.adj_list[v])


if __name__ == '__main__':
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_Edge('A', 'B')
    g.add_Edge('A', 'C')
    g.add_Edge('B', 'A')
    g.add_Edge('B', 'C')
    g.add_Edge('C', 'A')
    g.add_Edge('D', 'A')
    g.add_Edge('C', 'B')
    g.print_Graph()
    g.remove_edge('A', 'D')
    g.remove_edge('A', 'D')
    g.remove_edge('A', 'D')
    g.print_Graph()
    g.remove_vertex('C')
    g.remove_vertex('D')
    print("======")
    g.print_Graph()
    print(g)
