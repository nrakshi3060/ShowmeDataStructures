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


def dfs_search(root_node, target):
    visited = []
    stack = [root_node]

    while len(stack) > 0:
        current_node = stack.pop()

        visited.append(current_node.value)

        if current_node.value == target:
            return current_node

        for each_node in current_node.children:
            if each_node.value not in visited:
                stack.append(each_node)


def dfs_traversal(root_node):
    visited = []
    stack = [root_node]

    while len(stack) > 0:
        current_node = stack.pop()

        if current_node.value not in visited:
            print(current_node.value)
            visited.append(current_node.value)

        for each_node in current_node.children:
            if each_node.value not in visited:
                stack.append(each_node)


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

# l = dfs_search(nodeR, 'A')

# l = dfs_search(nodeR, 'B')
# print(l.value)

dfs_traversal(nodeR)
