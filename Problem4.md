# Problem4 - Active Directory
## Design
Solution for active directory is implemented by recursively walking through each group to find the user. Here the the given group to find the user can be considered as the Tree and each user as leaf. So we are using recursive approach to traverse each leaf of the tree to check if the given user exists or not.
## Time Complexity
**Time complexity is O(DEPTH  *  N)** 
This solution is implemented to visit all the user to check whether given user exists or not. So time taken to find out the given user exists or not is directly proportional to the depth of the root group and number users in each group.
where is the depth is the number of levels taken from the farthest user to the root group.
N is the number of users or groups in each directory.
## Space Complexity
**Space Complexity is O(DEPTH * N)**
Number of actively used data storage units increases with each recursive call and number of recursive call increases with depth of the given root folder and number of files in the root folder. 
where is the depth is the number of levels taken from the farthest user to the root group.
N is the number of users or groups in each directory.