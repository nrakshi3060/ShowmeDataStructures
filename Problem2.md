# Problem 2 - Finding Files
## Design
Finding files is by recursively checking each content of folder. Folder structure of given path can be compared to tree structure where files can be considered as leaves and given directory has root.
If the element of the folder is a folder, This folder is again recursively searched for the files with extension .c . Here the the time taken to print the file path is directly dependent on the number of elements in the folder.
Also, number of actively used storage units directly depends on the number of contents in the file. So, space complexity is O(n) where n is the number of files or directories in the folder.
## Time Complexity
**Time complexity is O(DEPTH  *  N)** 
This solution is implemented to visit all the elements to check whether it has  files with extension .c or not. So time taken to list all the files with given extension is directly proportional to the depth of the tree and number of files and directories.
where is the depth is the number of levels taken from the farthest file to the root directory.
N is the number of files or folders in each directory.
## Space Complexity
**Space Complexity is O(DEPTH * N)**
Number of actively used data storage units(call stack units) increases with each recursive call and number of recursive call increases with depth of the given root folder and number of files in the root folder. 
where is the depth is the number of levels taken from the farthest file to the root directory.
N is the number of files or folders in each directory.

 