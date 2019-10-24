###### **Problem3 - Huffman Coding**


List of tuples is built from lowest to highest frequencies by iterating through the given string. 
Huffman Tree  is built by assigning a binary code to each letter, using shorter codes for the more frequent letters.

Time complexity is O(n) where n is the number of unique characters. If there are n nodes, priority queue is dequeued  2*(n – 1) times. Deque takes O(n) times to deque in worst case scenario. So time complexity takes o(nlogn). 'n' here is the number of unique characters.