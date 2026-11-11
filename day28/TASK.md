# Day 28 — Build SupportIQ's LRU response cache (system design)

**Scenario:** **SupportIQ** caches recent KB lookups so repeated questions skip the model. Implement the eviction policy a reviewer would ask you to build on a whiteboard.

## Your task
Implement an `LRUCache` class plus two driver functions:

- `LRUCache(capacity)` with:
  - `get(key)` - return the stored value, or `-1` if the key is absent. A hit counts as a use (the key becomes most-recently-used).
  - `put(key, value)` - insert or update the key (most-recently-used). If this exceeds `capacity`, evict the least-recently-used key. A `capacity <= 0` stores nothing.
- `simulate(capacity, ops)` - run a fresh `LRUCache` through `ops` and return the list of results from every `get`. Each op is a list `['put', key, value]` or `['get', key]`.
- `cache_keys(capacity, ops)` - run `ops` on a fresh cache and return the remaining keys sorted ascending.

## Example
```python
ops = [['put','a',1], ['put','b',2], ['get','a'], ['put','c',3], ['get','b'], ['get','c']]
simulate(2, ops)   # -> [1, -1, 3]   (a hit; b evicted by c; c hit)
```

---
Edit `day28/solution.py`, commit & push, then click **Run Test** in the platform.
