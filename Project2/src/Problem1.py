class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return "(%s, %s)" % (self.key, self.value)


class LRUCache(object):
    def __init__(self, capacity=0):
        if not isinstance(capacity, int) or not capacity >= 0:
            print("Invalid value for Cache capacity")
            return
        self.capacity = capacity
        self.map = dict()
        self.head = None
        self.tail = None
        pass

    def print_elements(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.remove_node(node)
            self.add_node_at_top(node)
            print("Dict ==> {}".format(self.map))
            print("Linked List ==> {}".format(self.print_elements()))
            return node.value
        else:
            return -1
        pass

    def set(self, key, value):
        if self.capacity == 0:
            print("Cache size is 0! Please add the cache size greater than 0 to store an element")
            return
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove_node(node)
            self.add_node_at_top(node)
            return
        else:
            new_node = Node(key, value)
            if len(self.map) < self.capacity:
                self.add_node_at_top(new_node)
            else:
                del self.map[self.tail.key]
                self.remove_node(self.tail)
                self.add_node_at_top(new_node)

            self.map[key] = new_node
        print("Dict ==> {}".format(self.map))
        print("Linked List ==> {}".format(self.print_elements()))
        pass

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        if prev_node is not None:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node is not None:
            next_node.prev = prev_node
        else:
            self.tail = prev_node
        return

    def add_node_at_top(self, node):
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = self.head
        return


print("-----------------TestCase 1------------------------------")
our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("-----------------TestCase 2------------------------------")
cache1 = LRUCache(1)

cache1.set(1, 1)

print(cache1.get(1))  # returns 1
print(cache1.get(9))  # returns -1 because 9 is not present in the cache

cache1.set(5, 5)

print(cache1.get(5))  # returns 5

print("-----------------TestCase 3------------------------------")
cache2 = LRUCache()

cache2.set(1, 1)

print(cache2.get(1))  # returns -1
print(cache2.get(9))  # returns -1 because 9 is not present in the cache

cache2.set(5, 5)  # Cache size is 0! Please add the cache size greater than 0 to store an element

print(cache2.get(5))  # returns -1

print("-----------------TestCase 4------------------------------")
cache3 = LRUCache(None)  # Invalid value for Cache capacity

cache2.set(1, 1)  # Cache size is 0! Please add the cache size greater than 0 to store an element

print(cache2.get(1))  # returns -1
print(cache2.get(9))  # returns -1
