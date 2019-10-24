Problem3 - Huffman Coding

Take a string and determine the relevant frequencies of the characters.
List of tuples is built from lowest to highest frequencies. 
BHuffman Tree  is built by assigning a binary code to each letter, using shorter codes for the more frequent letters.

Time complexity is O(n) where n is the number of unique characters. If there are n nodes, priority queue is dequeued  2*(n – 1) times. Deque takes O(n) times to deque in worst case scenario. 