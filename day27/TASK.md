# Day 27 — SupportIQ self-consistency vote & structured-output check (frontier)

**Scenario:** To make the **SupportIQ** assistant more reliable you sample several reasoning chains and take a self-consistency vote, then validate that the chosen tool output matches a schema before the dispatcher acts on it.

## Your task
- `final_answer(chain)` - a chain is a string whose final answer follows the last `####` marker. Return that answer **stripped**; if there is no marker, return the whole chain stripped.
- `majority_vote(chains)` - extract each chain's `final_answer` and return the answer that occurs most often. Break ties by the answer string ascending. Return `None` for an empty list.
- `validate_output(obj, schema)` - `schema` maps each required key to a type name in `{'str','int','float','bool','list'}`. Return `True` only if `obj` is a dict whose keys **exactly** equal the schema's keys and whose values each match the named type. A `bool` must NOT be accepted where `'int'` is required.

## Example
```python
majority_vote(["q #### 4", "r #### 4", "s #### 5"])          # -> '4'
validate_output({"ticket_id": 7}, {"ticket_id": "int"})      # -> True
validate_output({"ticket_id": True}, {"ticket_id": "int"})   # -> False
```

---
Edit `day27/solution.py`, commit & push, then click **Run Test** in the platform.
