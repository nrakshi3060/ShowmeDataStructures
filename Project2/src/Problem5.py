import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode('utf-8') + str(self.timestamp).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.tail is None:
            return "Block chain is Empty !"
        cur_tail = self.tail
        out_string = ""
        while cur_tail:
            out_string += "[Data: {}, Hash: {}, DateTime: {}, Previous_Hash: {}]".format(cur_tail.data,
                                                                                         cur_tail.hash,
                                                                                         cur_tail.timestamp,
                                                                                         cur_tail.previous_hash) + " <- "
            cur_tail = cur_tail.previous
        return out_string

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, None)
            self.tail = self.head
        else:
            temp = self.tail
            self.tail = Block(timestamp, data, temp.previous_hash)
            self.tail.previous_hash = temp.previous_hash
            self.tail.previous = temp


def get_utc_time():
    utc = datetime.datetime.utcnow()
    return utc.strftime("%d/%m/%Y %H:%M:%S")


print("-------------------Test Case 1------------------------")
block_chain = LinkedList()
block_chain.append(get_utc_time(), "Some Information")
block_chain.append(get_utc_time(), "Another Information")
block_chain.append(get_utc_time(), "Some more Information")

print(block_chain)

print("-------------------Test Case 2------------------------")
block_chain = LinkedList()
for i in range(0, 1001):
    block_chain.append(get_utc_time(), "Block i".format(i))

print(block_chain)

print("-------------------Test Case 3------------------------")
block_chain = LinkedList()

print(block_chain)
