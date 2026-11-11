# Day 01 — Prioritise the SupportIQ discovery backlog

**Scenario:** During SupportIQ discovery the product team captured raw backlog items, each with a business `value` and an engineering `effort`, and needs them ranked before sprint planning.

## Your task
Implement two module-level functions.

1. `score_backlog(items)` — `items` is a list of dicts, each `{"id": str, "value": int, "effort": int}`. Compute each item's priority score as `round(value / effort, 2)`. Return a list of `(id, score)` tuples sorted by score **descending**, breaking ties by `id` **ascending**. Ignore (skip) any item whose `effort` is 0 or negative.

2. `validate_user_story(story)` — return `True` only when `story` is a non-empty string matching the shape `As a <role>, I want <goal>, so that <benefit>` (the three clauses separated by `, I want ` and `, so that `, each clause non-empty after stripping). Otherwise return `False`.

## Example
```python
score_backlog([{"id": "B2", "value": 8, "effort": 2},
               {"id": "B1", "value": 9, "effort": 3}])
# -> [('B2', 4.0), ('B1', 3.0)]
validate_user_story('As a support agent, I want refunds, so that customers stay')  # -> True
```


---
Edit `day01/solution.py`, commit & push, then click **Run Test** in the platform.
