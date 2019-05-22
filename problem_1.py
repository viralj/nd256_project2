import collections


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        
        # Initialize class variables _capacity and _cache
        self._capacity = capacity
        self._cache = collections.OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            # Getting value from cache by key and returning it
            value = self._cache.pop(key)
            self._cache[key] = value
            return value
        except KeyError:
            # If there was KeyError caught, returning -1
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        try:
            # Removing existing cache value by key
            self._cache.pop(key)
        except KeyError:
            # If there was KeyError caught and if length of cache is greater or equal capacity, removing oldest item 
            # from cache 
            if len(self._cache) >= self._capacity:
                self._cache.popitem(last=False)
        
        # Assigning value to the key
        self._cache[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(3)       # return -1
