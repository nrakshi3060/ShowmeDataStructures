class Heap(object):
    def __init__(self, intial_size=10):
        self.cbt = [None for _ in range(intial_size)]
        self.next_index = 0

    def _upheapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if child_element < parent_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _downheapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            paren_element = self.cbt[parent_index]
            left_child = None
            right_child = None

            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            min_element = paren_element

            if left_child is not None:
                min_element = min(paren_element, left_child)

            if right_child is not None:
                min_element = min(min_element, right_child)

            if min_element == paren_element:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = paren_element
                self.cbt[parent_index] = left_child
                parent_index = left_child_index
            elif min_element == right_child:
                self.cbt[right_child_index] = paren_element
                self.cbt[parent_index] = right_child
                parent_index = right_child_index

        pass

    def insert(self, value):
        self.cbt[self.next_index] = value

        self._upheapify()

        self.next_index += 1

        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(temp))]

            for i in range(len(temp)):
                self.cbt[i] = temp[i]

    def remove(self):
        self.next_index -= 1
        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]
        self.cbt[0] = last_element
        self._downheapify()

        self.cbt[self.next_index] = to_remove
        return to_remove
