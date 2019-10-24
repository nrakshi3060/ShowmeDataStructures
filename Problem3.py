import sys
from collections import deque
class Node(object):
        
    def __init__(self,value = None, frequency = None):
        self.value = value
        self.frequency = frequency
        self.bit_value = None
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right

    def set_bit_value(self, bit_value):
        self.bit_value = bit_value
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    def __repr__(self):
        return "Node(char = {}, freq={})".format(self.get_value(), self.frequency)
    
    def __str__(self):
        return "Node(char = {}, freq={})".format(self.get_value(), self.frequency)

class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    def is_empty(self): 
        return len(self.queue) == [] 
  
    def enq(self, node): 
        self.queue.append(node) 
  
    def deq(self): 
        try: 
            min = 0
            for i in range(len(self.queue)): 
                if self.queue[i].get_frequency() < self.queue[min].get_frequency(): 
                    min = i 
            item = self.queue[min] 
            del self.queue[min] 
            return item 
        except IndexError: 
            print() 
            exit() 
    
    def __len__(self):
        return len(self.queue)

class Tree():
    def __init__(self):
        self.root = None
        
    def set_root(self,value):
        self.root = Node(value)

    def set_root_node(self, node):
        self.root = node
        
    def get_root(self):
        return self.root
                    
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

                
        return s


def get_frequencies(data):
    dict1 = {}

    for char in data:
        if char in dict1:
            dict1[char] +=  1
        else:
            dict1[char] = 1
    
    p_queue = PriorityQueue()
    
    for char in dict1.keys():
        node = Node(char, dict1[char])
        p_queue.enq(node)

    return p_queue


def get_huffman_tree(data):
    huffman_tree = Tree() 
    p_queue = get_frequencies(data)
    new_node = Node()
    huffman_tree.set_root(new_node)

    while len(p_queue) > 1:
        node1 = p_queue.deq()
        node2 = p_queue.deq()
        new_frequency = node1.get_frequency() + node2.get_frequency()
        new_node.set_frequency(new_frequency)
        new_node.set_left_child(node1)
        new_node.set_right_child(node2)
        p_queue.enq(new_node)
        new_node = Node()

    huffman_tree.set_root_node(p_queue.deq())
    return huffman_tree

def get_encoded_table_helper(node, output, encoding_table, decoding_table):
    if node.get_right_child() == None and node.get_left_child() == None and node.get_value() != None:
        encoding_table[node.get_value()] = output
        decoding_table[output] = node.get_value()
        return 

    get_encoded_table_helper(node.get_left_child(), output + "0", encoding_table, decoding_table)
    get_encoded_table_helper(node.get_right_child(), output + "1", encoding_table, decoding_table)

def get_encoding_table(root):
    encoding_table = {}
    decoding_table = {}
    get_encoded_table_helper(root, "", encoding_table, decoding_table)
    return encoding_table, decoding_table

def get_encode_data(encoding_table, data):
    output = ""
    for char in data:
        output += encoding_table[char]
    return output
    pass

def get_decoded_data(decoding_table, data):
    output = ""
    enocded_bit = ""
    for bit in data:
        enocded_bit += bit
        if enocded_bit in decoding_table:
            output += decoding_table[enocded_bit]
            enocded_bit = ""

    return output



def huffman_encoding(data):
    huffman_tree = get_huffman_tree(data)
    root = huffman_tree.get_root()
    if root.get_left_child () is None and root.get_right_child() is None:
        table = {root.get_value() : '0'}, {'0' : root.get_value()}
    else:
        table = get_encoding_table(huffman_tree.get_root())
    print("Encoding table: {}".format(table[0]))
    output = get_encode_data(table[0], data)
    return output, huffman_tree
    pass


def huffman_decoding(data,tree):
    root = tree.get_root()
    if root.get_left_child() is None and root.get_right_child() is None:
        table = {root.get_value() : '0'}, {'0' : root.get_value()}
    else:
        table = get_encoding_table(tree.get_root())
    print("Decoding table: {}".format(table[1]))
    output = get_decoded_data(table[1], data)
    return output
    pass

if __name__ == "__main__":
    print("-----------------------Test Case 1------------------------------------")
    codes = {}

    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))


    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    print("-----------------------Test Case 2------------------------------------")

    a_great_sentence = "RRRRRRRRRRRRRRRRRRbr"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))


    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("-----------------------Test Case 3------------------------------------")

    a_great_sentence = "R"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))


    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("-----------------------Test Case 4------------------------------------")

    a_great_sentence = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))


    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
