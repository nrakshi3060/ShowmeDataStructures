Problem - 4 - Active Directory

Solution is implemented by recursively walking through each group to find the user.

So the time complexity is O(depth  * n) where n is the number of users. Space complexity O(depth * n) n is the number of users