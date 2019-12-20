class GraphNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        if node not in self.children:
            self.children.append(node)

    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def add_edge(self, node1, node2):
        if (node1 in self.nodes) and (node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes) and (node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_cild(node1)


def bfs_traversal(start_node):
    visited = []
    queue = [start_node]

    while len(queue) > 0:
        node = queue.pop(0)

        if node.value not in visited:
            print(node.value)
            visited.append(node.value)

        for child in node.children:
            if child.value not in visited:
                queue.append(child)
    return visited


def bfs_traversal_it(start_node):
    visited = []
    queue = [start_node]

    while len(queue) > 0:
        node = queue.pop(0)

        if node.value not in visited:
            visited.append(node.value)

        for each_node in node.children:
            if each_node.value not in visited:
                queue.append(each_node)
    return visited

nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)

# l = bfs_traversal(nodeG)
#
# print(l)

l1 = bfs_traversal_it(nodeG)
print(l1)


