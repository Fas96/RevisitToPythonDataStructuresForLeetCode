def traversal(start_vertex, graph):
    # queuing_strucute = new_queuing_structure()
    queuing_strucute = []
    queuing_strucute.push(start_vertex, None)
    explored_vertices = []
    routing_table = {}

    while len(queuing_strucute) > 0:
        current_vertex, parent = queuing_strucute.pop()
        if not (current_vertex in explored_vertices):
            explored_vertices.push(current_vertex)
            routing_table[current_vertex] = parent
            for neighbor in neighbors(graph, current_vertex):
                if neighbor not in explored_vertices:
                    queuing_strucute.push(neighbor, current_vertex)

    return explored_vertices, routing_table


graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [3, 5], 5: []}
if __name__ == '__main__':
    traversal(1, graph)
