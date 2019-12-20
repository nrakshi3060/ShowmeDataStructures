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
            node2.remove_child(node1)

def dfs_traversal_it(start_node):
    visited = []
    stack = [start_node]

    while len(stack) > 0:
        node = stack.pop()

        if node.value not in visited:
            visited.append(node.value)

        for each_node in node.children:
            if each_node.value not in visited:
                stack.append(each_node)

    return visited


def dfs_traversal_rec(start_node):
    visited = []
    __def_traversal_rec(start_node, visited)
    return visited

def __def_traversal_rec(node, visited):
    if node is None:
        return

    visited.append(node.value)

    for each_node in node.children:
        if each_node.value not in visited:
            __def_traversal_rec(each_node, visited)



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

l = dfs_traversal_it(nodeG)
print(l)

l1 = dfs_traversal_rec(nodeG)
print(l1)