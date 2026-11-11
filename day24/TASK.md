# Day 24 — Contract validation and breaking-change detection

**Scenario:** SupportIQ guards its ticket API with a lightweight contract so a new release cannot silently break downstream consumers.

## Your task
Implement two functions. A schema is `{'fields': {name: {'type': <t>, 'required': <bool>}}}` where `type` is one of `string,int,float,bool,list,dict` (`float` also accepts ints; a `bool` is **never** a valid `int` or `float`).

1. `validate_payload(payload, schema)` -> list: return a **sorted** list of `"missing:<field>"` for every required field absent from the payload and `"type:<field>"` for every present field whose value is the wrong type.
2. `detect_breaking_changes(old, new)` -> list: return a **sorted** list of findings: `"removed:<f>"` (field dropped), `"type_changed:<f>"` (type differs), `"now_required:<f>"` (was optional, now required), and `"added_required:<f>"` (brand-new required field). Adding an optional field is **not** breaking.

**Example:** `validate_payload({'priority':'high'}, {'fields':{'ticket_id':{'type':'string','required':True},'priority':{'type':'int','required':True}}})` -> `['missing:ticket_id', 'type:priority']`.

---
Edit `day24/solution.py`, commit & push, then click **Run Test** in the platform.
