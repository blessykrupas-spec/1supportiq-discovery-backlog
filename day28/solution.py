class LRUCache:
    """A fixed-capacity Least-Recently-Used cache with get(key) and put(key, value)."""
    def __init__(self, capacity):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError

def simulate(capacity, ops):
    """Drive an LRUCache through ops; return the list of results from every 'get'."""
    raise NotImplementedError

def cache_keys(capacity, ops):
    """Run ops on a fresh LRUCache; return the remaining keys sorted ascending."""
    raise NotImplementedError
