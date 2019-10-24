class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

    def __str__(self):
    	return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def get_dict(self):

    	if self.head is None:
    		return ()

    	node = self.head
    	output = {}
    	while node:
    		output[node.value] = node
    		node = node.next
    	return output

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    print("LinkedList 1: {}".format(llist_1))
    print("LinkedList 2: {}".format(llist_2))

    if llist_1.head is None:
        return llist_2

    if llist_2.head is None:
        return llist_1


    union_linked_list = LinkedList()
    set_1 = llist_1.get_dict().keys()
    set_2 = llist_2.get_dict().keys()
    llist_1_node = llist_1.head
    llist_2_node = llist_2.head


    for num in set_1:
        union_linked_list.append(num)

    for num in set_2:
        if num not in set_1:
            union_linked_list.append(num)

    return union_linked_list
    pass

def intersection(llist_1, llist_2):
    # Your Solution Here

    if llist_1.head is None or llist_2.head is None:
        return LinkedList()

    
    intersection_linked_list = LinkedList()

    dict1 = llist_1.get_dict()
    dict2 = llist_2.get_dict()

    for num in dict1:
        if (num in dict2) :
            intersection_linked_list.append(num)



    return intersection_linked_list

    pass

#________________________
print("+++++++++Test case 1++++++++++++")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print("union_linked_list = {}".format(union(linked_list_1,linked_list_2)))
print("intersection_linked_list = {}".format(intersection(linked_list_1,linked_list_2)))

#--------------------------
print("+++++++++Test case 2++++++++++++")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union_linked_list = {}".format(union(linked_list_3,linked_list_4)))
print("intersection_linked_list = {}".format(intersection(linked_list_3,linked_list_4)))
#_____________________________

print("+++++++++Test case 3++++++++++++")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [6,32,4,9,6,1,11,21,1]
element_2 = [3,2,4,35,6,65,6,4,3,23]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union_linked_list = {}".format(union(linked_list_3,linked_list_4)))
print("intersection_linked_list = {}".format(intersection(linked_list_3,linked_list_4)))

#-----------------------------------

print("+++++++++Test case 4++++++++++++")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [3,2,4,35,6,65,6,4,3,23]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union_linked_list = {}".format(union(linked_list_3,linked_list_4)))
print("intersection_linked_list = {}".format(intersection(linked_list_3,linked_list_4)))

#-----------------------------------

print("+++++++++Test case 5++++++++++++")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,2,3,4,5]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union_linked_list = {}".format(union(linked_list_3,linked_list_4)))
print("intersection_linked_list = {}".format(intersection(linked_list_3,linked_list_4)))

#-----------------------------------

print("+++++++++Test case 6++++++++++++")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("union_linked_list = {}".format(union(linked_list_3,linked_list_4)))
print("intersection_linked_list = {}".format(intersection(linked_list_3,linked_list_4)))
