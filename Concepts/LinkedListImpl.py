"""
Linked List Implementation
Implement a linked list class. Your class should be able to:

prepend
Append data to the tail of the list and prepend to the head
Search the linked list for a value and return the node
Remove a node
Pop, which means to return the first node's value and delete the node from the list
Insert data at some position in the list
Return the size (length) of the linked list
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp

    def search(self, value):
        if self.head is None:
            return

        node = self.head

        while node is not None:
            if node.value == value:
                return node
            node = node.next
        raise ValueError("Value not found in the list")

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head

        while node.next is not None:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next
        raise ValueError("Value not found in the list")

    def pop(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next
        return value

    def size(self):
        if self.head is None:
            return 0
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def to_list(self):
        if self.head is None:
            return []
        output = []
        node = self.head
        while node is not None:
            output.append(node.value)
            node = node.next
        return output

    def insert_value(self, value, pos):
        if pos == 0:
            self.prepend(value)
            return
        if pos > (self.size()-1):
            self.append(value)
            return

        node = self.head

        count = 0

        while node is not None:
            if (pos-1) == count:
                temp = Node(value)
                temp.next = node.next
                node.next = temp
                return
            node = node.next


## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert
linked_list.insert_value(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert_value(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert_value(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"
