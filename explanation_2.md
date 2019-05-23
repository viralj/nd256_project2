### Explanation problem 2 : Finding Files

For this problem, I am first checking if path is valid and exit. If not, simply return empty list. If it is valid path 
and exist, I am using two lists to hold information in it. One is to hold directories to walk through and second is the 
value of files including path. Using while loop, I am removing first value of directories and getting all items from 
that directory. After that, for each item I am checking if its directory or not and if its directory, add it to 
directories list, else check for file and with extension by suffix passed.


Time complexity is `O(depth * average number of directories in each level)` and space complexity os `O(depth)`.
