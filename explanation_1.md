### Explanation problem 1 : Least Recently Used Cache

For this problem, I have used `OrderDict` from `collections` module. After instantiating class with max capacity, we 
can use `set()` method to set cache and assign value at specific keys. All keys are `None` until assigned. It will try 
to assign value to given key by removing the value if assigned else after checking capacity and key item is removed 
from dict and value is assigned again. To get value of the key, we can use `get()` method.

Time complexity of `get()` is `O(1)` and of `set()` is `O(1)`. Space complexity of the LRU Cache is `O(n)`.
