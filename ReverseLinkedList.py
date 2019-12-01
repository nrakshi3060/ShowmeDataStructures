class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    curr = head
    next_node = None
    new = None

    while curr is not None:
        next_node = curr.next
        curr.next = new
        new = curr
        curr = next_node
    return new
