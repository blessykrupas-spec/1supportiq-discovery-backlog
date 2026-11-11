# Day 03 — Aggregate SupportIQ tickets per category with SQL

**Scenario:** A SupportIQ analyst needs per-category ticket volumes straight from SQL (practised locally with the standard-library `sqlite3`, mirroring the Postgres query you would run in production).

## Your task
Use the standard-library `sqlite3` module (an in-memory database) in two functions.

1. `category_counts(tickets)` — `tickets` is a list of dicts like `{"id": str, "category": str}`. Create a `tickets` table, insert the rows, then run a `GROUP BY category` query. Return a list of `(category, count)` tuples sorted by `count` **descending**, ties broken by `category` **ascending**.

2. `top_category(tickets)` — return the single category string with the most tickets (ties broken by `category` ascending). Return `None` for an empty list.

## Example
```python
rows = [{'id':'T1','category':'billing'}, {'id':'T2','category':'billing'}, {'id':'T3','category':'technical'}]
category_counts(rows)  # -> [('billing', 2), ('technical', 1)]
top_category(rows)     # -> 'billing'
```


---
Edit `day03/solution.py`, commit & push, then click **Run Test** in the platform.
