# Day 12 — SupportIQ: Validate LLM JSON and Retry Backoff

**Scenario:** SupportIQ calls an LLM to tag each ticket and must treat the model as an unreliable component: validate its JSON against a schema and retry failed calls on an exponential backoff.

## Your task
Standard library only (`json`). Implement:

- `parse_json(text)` -> `dict | None`: the parsed object, or `None` if `text` is not valid JSON or is not a JSON object.
- `validate_output(text, schema)` -> `list[str]`: parse `text`; if it is not a valid JSON object return `['invalid_json']`. Otherwise return a sorted list of `'missing:<field>'` for absent fields and `'type:<field>'` for wrong types. `schema` maps a field to one of `'str'`, `'int'`, `'float'`, `'bool'`, `'list'` (note: a JSON boolean is NOT a valid `int`/`float`).
- `backoff_schedule(base, factor, retries, cap)` -> `list[float]`: `[round(min(cap, base * factor ** i), 2) for i in range(retries)]`.

**Example:** `backoff_schedule(0.5, 2.0, 5, 4.0)` returns `[0.5, 1.0, 2.0, 4.0, 4.0]`.

---
Edit `day12/solution.py`, commit & push, then click **Run Test** in the platform.
