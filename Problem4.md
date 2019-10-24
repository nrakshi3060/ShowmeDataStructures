Problem - 4 - Active Directory

Solution is implemented by recursively walking through each group to find the user.
So in worst case need to visit every user so time complexity is directly proportional to number of users. In worst case number of actively storage units to store all the users is directly proportional to the number of users. 
So the time complexity is O(n) where n is the number of users. Space complexity O(n) n is the number of users