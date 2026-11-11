# Day 02 — Typed order lookup with a domain exception

**Scenario:** The SupportIQ order service must never return a wrong order silently — unknown ids raise a typed domain error, and malformed input is rejected up front.

## Your task
Implement the following at module level.

1. A custom exception class `OrderNotFoundError(Exception)`.

2. `lookup_order(orders, order_id)` — `orders` is a list of dicts like `{"order_id": str, "status": str, "total": float}`. If `order_id` is not a non-empty string, raise `ValueError`. If no order matches, raise `OrderNotFoundError`. Otherwise return the matching order dict.

3. `describe_order(orders, order_id)` — call `lookup_order` and return the string `"<status> order <order_id> totaling <total>"`. If the order is missing, catch `OrderNotFoundError` and return `"Order <order_id> not found"`.

4. `raises_not_found(orders, order_id)` — return `True` if `lookup_order` raises `OrderNotFoundError` for that id, else `False`.

## Example
```python
ORDERS = [{'order_id': 'O1', 'status': 'shipped', 'total': 120.0}]
describe_order(ORDERS, 'O1')   # -> 'shipped order O1 totaling 120.0'
describe_order(ORDERS, 'O9')   # -> 'Order O9 not found'
```


---
Edit `day02/solution.py`, commit & push, then click **Run Test** in the platform.
