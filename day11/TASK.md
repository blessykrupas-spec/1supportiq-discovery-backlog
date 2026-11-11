# Day 11 — SupportIQ: Promotion Gates and Batch Scoring

**Scenario:** SupportIQ only ships a new classifier when it clears a promotion gate against the current production model, then it batch-scores the day's open tickets.

## Your task
Standard library only. Implement:

- `should_promote(candidate, prod, metric, min_delta)` -> `bool`: `True` iff `candidate[metric] >= prod[metric] + min_delta`; `False` if the metric is missing from either dict.
- `passes_gates(candidate, gates)` -> `bool`: `gates` maps a metric to `(op, value)` with `op` in `{'min','max'}`. Return `True` iff every gate holds (`'min'` requires the metric `>= value`, `'max'` requires `<= value`); a missing metric fails.
- `batch_predict(rows, threshold)` -> `list[int]`: each row is `{"id","score"}`; return the sorted list of ids whose `score >= threshold`.

**Example:** with candidate f1 `0.86` and prod f1 `0.83`, `should_promote(candidate, prod, 'f1', 0.02)` returns `True`.

---
Edit `day11/solution.py`, commit & push, then click **Run Test** in the platform.
