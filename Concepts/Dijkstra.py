import math


class GraphEdge:
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2, distance)
            node2.remove_child(node1, distance)


def diijkstra(start_node, end_node):
    distance_dict = {node: math.inf for node in graph.nodes}
    distance_dict[start_node] = 0
    shortest_path_dict = {}

    while distance_dict:
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]

        shortest_path_dict[current_node] = distance_dict.pop(current_node)

        for edge in current_node.edges:
            if edge.node in distance_dict:
                new_node_distance = node_distance + edge.distance
                if new_node_distance < distance_dict[edge.node]:
                    distance_dict[edge.node] = new_node_distance
    return shortest_path_dict[end_node]


node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_u, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_u, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_d, 4)
graph.add_edge(node_c, node_u, 6)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_a, 7)
graph.add_edge(node_i, node_c, 4)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_c, 5)
graph.add_edge(node_t, node_y, 5)
graph.add_edge(node_y, node_i, 4)
graph.add_edge(node_y, node_t, 5)

print(diijkstra(node_u, node_y))
