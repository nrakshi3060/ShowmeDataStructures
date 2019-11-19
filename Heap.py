class Heap:
    def __init__(self, intial_size=10):
        self.cbt = [None for _ in range(intial_size)]
        self.next_index = 0

    def size(self):
        return self.next_index + 1

    def get_minimum(self):
        return self.cbt[0]

    def is_empty(self):
        return self.size() == 0

    def up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element
                child_index = parent_index
            else:
                break

        pass

    def down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            parent_element = self.cbt[parent_index]
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            left_child = None
            right_child = None
            min_element = parent_element

            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            if left_child is not None:
                min_element = min(parent_element, left_child)

            if right_child is not None:
                min_element = min(min_element, right_child)

            if min_element == parent_element:
                return

            if min_element == left_child:
                self.cbt[parent_index] = left_child
                self.cbt[left_child_index] = parent_element
                parent_index = left_child_index
            elif min_element == right_child:
                self.cbt[parent_index] = right_child
                self.cbt[right_child_index] = parent_element
                parent_index = right_child_index

        pass

    def insert(self, data):
        self.cbt[self.next_index] = data

        self.up_heapify()

        self.next_index += 1

        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for i in range(len(temp)):
                self.cbt[i] = temp[i]

        pass

    def remove(self):
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        self.cbt[0] = last_element
        self.cbt[self.next_index] = None

        self.down_heapify()
        return to_remove

        pass


heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)

print(heap.cbt)
print('Inserted elements: {}'.format(elements))
print(heap.cbt)
print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print(heap.cbt)

print('Call is_empty: {}'.format(heap.is_empty()))
