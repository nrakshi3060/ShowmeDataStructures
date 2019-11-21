# Problem5 - Blockchain
## Design
Block chain is implemented with LinkedList class. Linkedlist is intialized with head and tail set to none. Head points to the start of the chain and tail point the end of the chain.
**Append:** is implemented by keeping track of the tail, each time new element needs to be appended will be added by pointing the next of tail to new element and tail will be updated to point to the newly added element.  
**_str_:** is implemented by looping through all the elements from head to the tail and appended to string which will be returned back. 
## Time Complexity
**Time complexity of Append is O(1)** 
Append method takes O(1) time complexity to add a block to the end of the chain.
**Time complexity of Printing Block chain is O(n)** 
In order to print block chain the program needs to visit all the blocks in the block chain so the time complexity is linear.
## Space Complexity
**Space Complexity is O(N)**
Number of actively used nodes depends on the number of blocks in the chain. So the space complexity is O(n)