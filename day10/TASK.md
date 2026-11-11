# Day 10 — SupportIQ: A Minimal Experiment Run Store

**Scenario:** While tuning the SupportIQ classifier, the team logs every training run's params and metrics to a lightweight in-memory store (an MLflow stand-in) and asks it for the best run.

## Your task
A `store` is a `list` of run dicts `{"run_id", "params", "metrics"}`. Implement (standard library only):

- `record_run(store, params, metrics)` -> `int`: append a run with `run_id = len(store) + 1` (storing copies of `params`/`metrics`) and return the new `run_id`.
- `best_run(store, metric, mode="max")` -> `int`: return the `run_id` optimizing `metric` (`mode` is `'max'` or `'min'`), breaking ties by the smallest `run_id`; return `-1` if no run recorded that metric.
- `get_metric(store, run_id, metric)` -> `float | None`: `round(value, 2)` for that run/metric, or `None` if the run is absent or that metric was not logged for the run.

**Example:** with runs scoring f1 = 0.83 (run 2) and f1 = 0.83 (run 3), `best_run(store, 'f1')` returns `2`.

---
Edit `day10/solution.py`, commit & push, then click **Run Test** in the platform.
