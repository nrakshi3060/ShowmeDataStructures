class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap(object):
    def __init__(self, intial_size=10):
        self.bucket_array = [None for _ in range(intial_size)]
        self.num_entries = 0
        self.p = 37

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)
        new_node = Node(key, value)
        node = self.bucket_array[bucket_index]

        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next

        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

        load_factor = self.num_entries / len(self.bucket_array)

        if load_factor >= 0.7:
            self.num_entries = 0
            self._rehash()
        pass

    def get(self, key):
        bucket_index = self.get_bucket_index(key)
        node = self.bucket_array[bucket_index]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None
        pass

    def _rehash(self):
        old_bucket_array = self.bucket_array
        old_num_buckets = len(self.bucket_array)
        new_num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(new_num_buckets)]

        for head in old_bucket_array:
            while head:
                key = head.key
                value = head.value
                self.put(key, value)
                head = head.next
        return

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0

        for char in key:
            ascii_value = ord(char)
            hash_code += ascii_value * current_coefficient
            hash_code = hash_code % num_buckets
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets
        return hash_code % num_buckets

