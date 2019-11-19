# Problem 1
## Design
LRU cache here is implemented using dictionary and doubly linked list. Doubly linked list is setup in such way that the head has the most recently used element and tail has least recently used element. Reason for using dictionary because it supports O(1) look up. Each time an element is accessed, that element node in linked list is removed and added to the top of the list. Also, during adding elements to the cache if the size overflows then the least recently used element node(tail of the list) will be removed. Removal of node and addition of node at top in doubly linked list takes O(1) time complexity. Time complexity of get and set methods in this implementation takes O(1). Space complexity is directly proportional to the size of the cache as the cache size increases the number of actively used Doubly linked list nodes and dictionary entries increases. 
## Time Complexity
### Get :
Time complexity of Get : **O(1)**
### Set :
Time complexity of Set : **O(1)**
## Space Complexity
Space complexity : **O(N)**