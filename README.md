# nd256_project2

Udacity's Data Structures &amp; Algorithms Nanodegree program project 2

------------------------------------------------------

## Problem 1
# Least Recently Used Cache

We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.

Your job is to use appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:

    class LRU_Cache(object):
    
        def __init__(self, capacity):
            # Initialize class variables
            pass
    
        def get(self, key):
            # Retrieve item from provided key. Return -1 if nonexistent. 
            pass
    
        def set(self, key, value):
            # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
            pass
    
    our_cache = LRU_Cache(5)
    
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.get(1)       # returns 1
    our_cache.get(2)       # returns 2
    our_cache.get(3)       # return -1

------------------------------------------------------

## Problem 2
# Finding Files

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded [here](https://s3.amazonaws.com/udacity-dsand/testdir.zip):

    ./testdir
    ./testdir/subdir1
    ./testdir/subdir1/a.c
    ./testdir/subdir1/a.h
    ./testdir/subdir2
    ./testdir/subdir2/.gitkeep
    ./testdir/subdir3
    ./testdir/subdir3/subsubdir1
    ./testdir/subdir3/subsubdir1/b.c
    ./testdir/subdir3/subsubdir1/b.h
    ./testdir/subdir4
    ./testdir/subdir4/.gitkeep
    ./testdir/subdir5
    ./testdir/subdir5/a.c
    ./testdir/subdir5/a.h
    ./testdir/t1.c
    ./testdir/t1.h

Python's os module will be useful—in particular, you may want to use the following resources:

[`os.path.isdir(path)`](https://docs.python.org/3.7/library/os.path.html#os.path.isdir)

[`os.path.isfile(path)`](https://docs.python.org/3.7/library/os.path.html#os.path.isfile)

[`os.listdir(directory)`](https://docs.python.org/3.7/library/os.html#os.listdir)

[`os.path.join(...)`](https://docs.python.org/3.7/library/os.path.html#os.path.join)

# Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

Here is some code for the function to get you started:


    def find_files(suffix, path):
        """
        Find all files beneath path with file name suffix.
    
        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.
    
        There are no limit to the depth of the subdirectories can be.
    
        Args:
        suffix(str): suffix if the file name to be found
        path(str): path of the file system
    
        Returns:
        a list of paths
        """
        return None

OS Module Exploration Code
`#Locally save and call this file ex.py`

`#Code to demonstrate the use of some of the OS modules in python`

    import os

    # Let us print the files in the directory in which you are running this script
    print (os.listdir("."))

    # Let us check if this file is indeed a file!
    print (os.path.isfile("./ex.py"))

    # Does the file end with .py?
print ("./ex.py".endswith(".py"))
