class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_loop(head):
    if head is None:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True

    return False
