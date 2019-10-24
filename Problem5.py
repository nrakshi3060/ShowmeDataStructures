import hashlib
import datetime
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_tail = self.tail
        out_string = ""
        while cur_tail:
            out_string += "[Data: {}, Hash: {}, DateTime: {} ]".format(cur_tail.data, cur_tail.hash, cur_tail.timestamp) + " <- "
            out_string +="\n"
            cur_tail = cur_tail.previous_hash
        return out_string

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.tail = self.head
        else:
            temp = self.tail
            self.tail = Block(timestamp, data, temp)
            self.tail.previous_hash = temp

def get_utc_time():
      utc = datetime.datetime.utcnow()
      return utc.strftime("%d/%m/%Y %H:%M:%S")


block_chain = LinkedList()
block_chain.append(get_utc_time(), "Some Information")
block_chain.append(get_utc_time(), "Another Information")
block_chain.append(get_utc_time(), "Some more Information")

print(block_chain)