# Problem6 -  Union and Intersection of Two Linked Lists
## Design
In this problem get_dict is implemented to convert the linked list to dictionary. Reason for using dictionary is because it provides O(1) complexity to access the elements. Once it is converted to dict it becomes easy to perform union and intersection. 
To find intersection of two linked list it would take n plus m iterations to convert them to dictionary and to loop over them to find intersecting elements. In union method it takes n plus m iterations to convert the linked lists to set and then iterate over n plus m elements to create union linkedlist.

## Time Complexity
**Time complexity of Union is O(m + n)** 
where m is the length of linkedlist1 and n is the length of linkedlist2.
Time taken to convert linkedlist1 and linkedlist2 to set and then it is checked against the sets to add it to the Unionlinkedlist is directly proportional to length of both linked lists.
**Time complexity of intersection is O(m + n)** 
where m is the length of linkedlist1 and n is the length of linkedlist2.
Time taken to convert linkedlist1 and linkedlist2 to dictionary and then it is checked against the dictionary to add it to the intersectionlinkedlist is directly proportional to length of both linked lists.
**Space complexity of Union is O(m + n)** 
where m is the length of distinct elements in linkedlist1 and n is the length of distinct elements in linkedlist2.
Number of actively used storage units is  directly proportional to number of unique elements in linkedlist1 and linkedlist2. So time complexity is directly propotional to the length of unique elements in both linked lists O(m + N).
**Space complexity of intersection is O(n)** 
where n is the number of distinct elements which are common to both linkedlist1 and linkedlist2.
Number of actively used storage units is  directly proportional to distinct elements which are common to both linkedlist1 and linkedlist2. So time complexity is directly propotional to distinct elements which are common to both linkedlists.