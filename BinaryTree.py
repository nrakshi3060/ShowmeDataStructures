class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value
        return

    def get_value(self):
        return self.value

    def set_right_child(self, value):
        self.right = Node(value)
        return

    def set_left_child(self, value):
        self.left = Node(value)
        return

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        return

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return len(self.items) == 0


class State(object):
    def __init__(self, node=None):
        self.node = node
        self.visited_left = False
        self.visited_right = False


class Queue(object):
    def __init__(self):
        self.items = []

    def enq(self, data):
        self.items.append(data)
        return

    def deq(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


def pre_order_with_stack(tree: Tree):
    visit_order = []
    stack = Stack()
    node = tree.get_root()
    state = State(node)
    visit_order.append(node.get_value())
    stack.push(state)
    while node:
        if node.has_left_child() and not state.visited_left:
            state.visited_left = True
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = state(node)
            stack.push(state)
        elif node.has_right_child() and not state.visited_right:
            state.visited_right = True
            node = node.get_right_child()
            visit_order.append(node.get_right_child())
            state = state(node)
            stack.push(state)
        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = stack.top()
            else:
                node = None
    return visit_order


def pre_order_with_recursion(tree: Tree):
    visit_order = []
    node = tree.get_root()

    def traverse(node):
        if node:
            visit_order.append(node.get_value())

            traverse(node.get_left_child())

            traverse(node.get_right_child())

    traverse(node)
    return visit_order


def in_order_with_recursion(tree: Tree):
    visit_order = []
    node = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())

            visit_order.append(node.get_value())

            traverse(node.get_right_child())

    traverse(node)
    return visit_order


def post_order_with_recursion(tree: Tree):
    visit_order = []
    node = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())

            traverse(node.get_right_child())

            visit_order.append(node.get_value())

    traverse(node)
    return visit_order


def bfs(tree: Tree):
    visit_order = []
    queue = Queue()
    node = tree.get_root()
    queue.enq(node)

    while not queue.is_empty():
        node = queue.deq()

        if node.has_left_child():
            queue.enq(node.get_left_child())
        if node.has_right_child():
            queue.enq(node.get_right_child())
        visit_order.append(node.get_value())
    return visit_order

tree = Tree("apple")
tree.get_root().set_left_child("banana")
tree.get_root().set_right_child("cherry")
tree.get_root().get_left_child().set_left_child("dates")

print("BFS ==> {}".format(bfs(tree)))

print("DFS Pre-order ==> {}".format(pre_order_with_recursion(tree)))

print("DFS In-order ==> {}".format(in_order_with_recursion(tree)))

print("DFS Post-order ==> {}".format(post_order_with_recursion(tree)))

