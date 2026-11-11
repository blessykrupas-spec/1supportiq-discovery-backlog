# Day 16 — Classifier metrics and an output guardrail for SupportIQ

**Scenario:** SupportIQ must measure its intent-classifier's quality and guard the assistant's replies from leaking banned language or customer PII.

## Your task
Implement two functions (standard library only):

- `prf1(y_true, y_pred)` — parallel lists of binary labels (`1` = positive). Return a tuple `(precision, recall, f1)`, each a float **rounded to 2 decimals**. Use `precision = tp/(tp+fp)`, `recall = tp/(tp+fn)`, `f1 = 2PR/(P+R)`. Any metric with a zero denominator is `0.0`.
- `is_blocked(text, banned)` — return `True` if `text` must be blocked: it contains any `banned` term (case-insensitive substring), **or** an email address, **or** a run of 10 or more consecutive digits (phone/card-like PII). Otherwise `False`.

**Example:**
```
prf1([1,1,1,0,0], [1,1,0,1,1])     -> (0.5, 0.67, 0.57)
is_blocked("call 9876543210", [])  -> True
is_blocked("happy to help", ["idiot"]) -> False
```


---
Edit `day16/solution.py`, commit & push, then click **Run Test** in the platform.
