Problem 2 - Finding Files

This problem is implemented by recursively checking each content of the folder. If the element of the folder is a folder, This folder is again recursively searched for the files with extension .c . Here the the time taken to print the file path is directly dependent on the number of elements in the folder. It has to visit all the elements to check whether its a file with extension .c or not. So time complexity is O(n)

