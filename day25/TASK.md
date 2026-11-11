# Day 25 — SupportIQ latency SLOs: percentiles & slowest stage (load testing)

**Scenario:** You load-test the **SupportIQ** assistant and must report latency SLOs and find which pipeline stage is the bottleneck.

## Your task
Implement three module-level functions:

- `percentiles(latencies)` - given a list of request latencies in milliseconds, return the tuple `(p50, p95, p99)` using the **nearest-rank** method: sort ascending, and for percentile `p` take the value at 1-based rank `ceil(p/100 * n)` (clamped to `[1, n]`). Round each result with `round(x, 2)`. Raise `ValueError` on an empty list.
- `over_budget(latencies, budget_ms)` - return the integer count of latencies **strictly greater** than `budget_ms`.
- `slowest_stage(stages)` - `stages` maps a stage name to a list of per-request latencies. Return the name of the stage with the highest **mean** latency; break ties by stage name ascending. Return `None` when `stages` is empty.

## Example
```python
percentiles([12, 20, 35, 40, 55, 60, 75, 90, 110, 500])  # -> (55.0, 500.0, 500.0)
slowest_stage({'retrieve': [30, 32, 28], 'generate': [120, 140, 100]})  # -> 'generate'
```

---
Edit `day25/solution.py`, commit & push, then click **Run Test** in the platform.
