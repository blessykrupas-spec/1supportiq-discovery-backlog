# Day 08 — SupportIQ: Data-Quality and Schema-Drift Checks

**Scenario:** Before SupportIQ trusts a nightly ticket batch, its observability job checks column null-rates, batch freshness, and whether the schema drifted from the previous run.

## Your task
Each row is a dict. Implement (standard library only):

- `null_rate(rows, field)` -> `float`: fraction of rows whose `field` is `None` or `""`, as `round(x, 2)`; `0.0` for empty input.
- `is_fresh(rows, now_ts, max_age_sec)` -> `bool`: `True` when `now_ts - max(row['ts'])` is `<= max_age_sec`; `False` for empty input.
- `schema_drift(old_rows, new_rows)` -> `tuple`: `(added, removed)` where each is the sorted list of column names gained / lost going from the old row-set to the new one (union of keys across rows).

**Example:** if old rows have keys `{id, category}` and new rows have `{id, category, sentiment}`, then `schema_drift(...)` returns `(['sentiment'], [])`.

---
Edit `day08/solution.py`, commit & push, then click **Run Test** in the platform.
