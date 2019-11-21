# Problem3 - Huffman Coding
## Design
List of tuples is built from lowest to highest frequencies by iterating through the given string. 
Huffman Tree  is built by assigning a binary code to each letter, using shorter codes for the more frequent letters.
## Time Complexity
**Time complexity is O(nlogn)** 
where n is the number of unique characters in the given string.
If there are n nodes, priority queue is dequeued  2*(n – 1) times. Deque takes O(logn) times to deque in worst case scenario.
so time complexity will be O(n) = 2nlogn - logn. For large inputs logn and 2n can be neglected. So time complexity will be O(nlogn)
## Space Complexity
**Space complexity is O(n)**
where n is the number of unique characters in the given string.
Number of actively used data storage units depends on the number of unique characters in the string.