# Day 06 — Order a SupportIQ task DAG and tally retries

**Scenario:** SupportIQ's nightly flow is a DAG of tasks (ingest tickets, enrich, score, notify). The orchestrator must schedule tasks in dependency order, refuse to run a cyclic flow, and report retry totals.

## Your task
`deps` is a dict mapping each task name to a list of prerequisite task names that must finish first.

1. `has_cycle(deps)` — return `True` if the dependency graph contains a cycle, else `False`.

2. `topological_order(deps)` — return the lexicographically smallest valid topological order as a list (when several tasks are ready, pick the alphabetically smallest first). If the graph has a cycle, return `[]`.

3. `count_retries(runs)` — `runs` is a list of dicts `{"task": str, "attempts": int}`; retries for a run are `attempts - 1` (never negative). Return the total number of retries across all runs as an int.

## Example
```python
deps = {'score': ['enrich'], 'enrich': ['ingest'], 'ingest': [], 'notify': ['score']}
topological_order(deps)  # -> ['ingest', 'enrich', 'score', 'notify']
has_cycle({'a': ['b'], 'b': ['a']})  # -> True
count_retries([{'task':'ingest','attempts':3}, {'task':'score','attempts':1}])  # -> 2
```


---
Edit `day06/solution.py`, commit & push, then click **Run Test** in the platform.
