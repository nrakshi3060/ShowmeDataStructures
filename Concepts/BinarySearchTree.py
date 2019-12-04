class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree(object):
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def comparision(self, node, new_node):
        if node.value == new_node.value:
            return 0
        if new_node.value < node.value:
            return -1
        if new_node.value > node.value:
            return 1

    def insert_with_loop(self, value):
        node = self.get_root()

        while True:
            compare = self.comparision(node, Node(value))

            if compare == 1:
                node.set_value(value)
            elif compare == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(Node(value))
                    break
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(Node(value))


