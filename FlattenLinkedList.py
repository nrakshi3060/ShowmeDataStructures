# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    def __str__(self):
        node = self.head
        out_str = ""
        while node:
            out_str += str(node.value) + "-->"
            node = node.next
        return out_str


def merge(list1, list2):
    if list1.head is None and list2.head is None:
        return list1

    if list1 is None or list1.head is None:
        return list2

    if list2 is None or list2.head is None:
        return list1
    list1_node = list1.head
    list2_node = list2.head
    output_list = LinkedList(None)
    while list1_node and list2_node:
        if list1_node is None:
            output_list.append(list2_node)
            list2_node = list2_node.next
        elif list2_node is None:
            output_list.append(list1_node)
            list1_node = list1_node.next
        elif list1_node.value <= list2_node.value:
            output_list.append(list1_node)
            list1_node = list1_node.next
        else:
            output_list.append(list2_node)
            list2_node = list2_node.next
    return output_list
    pass


class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))


linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
print(nested_linked_list.flatten())


