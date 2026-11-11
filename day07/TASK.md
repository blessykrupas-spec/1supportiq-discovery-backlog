# Day 07 — SupportIQ: Build a Ticket Feature Table in SQL

**Scenario:** SupportIQ's analytics layer turns raw `tickets` into a per-category feature table and runs a data test that must fail loudly when a billing ticket arrives without an `order_id`.

## Your task
Using the standard-library `sqlite3` module (load the ticket dicts into an in-memory table), implement:

- `category_features(tickets)` -> `list[tuple]`: one row per category, `(category, ticket_count, round(avg_priority, 2), high_priority_count)` where `high_priority_count` counts tickets with `priority >= 4`. Rows sorted ascending by category.
- `failing_billing_rows(tickets)` -> `int`: a data test returning how many `category == 'billing'` tickets have a NULL or empty-string `order_id`.

Each ticket is a dict `{"id","text","category","order_id","priority"}` (`order_id` may be `None`).

**Example:** for tickets with billing priorities 3 and 5 (one missing `order_id`), `category_features(...)` includes `('billing', 2, 4.0, 1)` and `failing_billing_rows(...)` returns `1`.

---
Edit `day07/solution.py`, commit & push, then click **Run Test** in the platform.
